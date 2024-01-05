from telebot import types
import requests


def format_film_details(film):
    details = [
        f"🎬 Title: {film['title']}",
        f"📅 Release Date: {film['release_date']}",
        f"🌍 Country: {film['country']}",
        f"🎭 Genre: {film['genre']}",
        f"🌟 Cast: {film['actors']}",
        f"🔞 Age Limit: {film['age_limit']}",
    ]
    if film.get('poster'):
        details.append(f"🖼️ Poster: {film['poster']}")
    if film.get('films_to_recommend'):
        details.append(f"\n\n🔎You might also enjoy: {', '.join(film['films_to_recommend'])}")

        keyboard = types.InlineKeyboardMarkup()
        for title in film['films_to_recommend']:
            callback_button = types.InlineKeyboardButton(text=title, callback_data=f'rec_{title}')
            keyboard.add(callback_button)
        return details, keyboard
    return details, None


def create_telegram_user(message):
    api_url = 'http://127.0.0.1:8000/api/telegram_users/'

    user_data = {
        'name': message.from_user.first_name,
        'surname': message.from_user.last_name or '',
        'tg_username': message.from_user.username or '',
        'tg_id': str(message.from_user.id),
    }
    try:
        response = requests.post(api_url, data=user_data)
        response.raise_for_status()  # This will raise an HTTPError if HTTP request is unsuccessful
    except Exception as e:
        return e
    return response


def create_film(film):
    api_url = 'http://127.0.0.1:8000/api/films/'

    film_data = {
        'title': film.get('title'),
        'poster_url': film.get('poster'),
        'release_date': film.get('release_date'),
        'country': film.get('country'),
        'genre': film.get('genre'),
        'actors': film.get('actors'),
        'age_limit': film.get('age_limit'),
        'recommendations': ', '.join(film.get('movies_to_recommend', []))
    }

    try:
        response = requests.post(api_url, data=film_data)
        response.raise_for_status()  # This will raise an HTTPError if HTTP request is unsuccessful
    except requests.exceptions.RequestException as e:
        return None, e
    return response.json(), None


def set_user_state(chat_id, state):
    api_url = 'http://127.0.0.1:8000/api/user_states/'
    data = {'chat_id': chat_id, 'state': state}
    try:
        response = requests.post(api_url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, e
    return response.json(), None


def get_user_state(chat_id):
    api_url = 'http://127.0.0.1:8000/api/user_states/'
    params = {'search': chat_id}
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            return response.json()[0]
        return None
    except requests.exceptions.RequestException as e:
        return None


# def get_or_create_telegram_user(message):
#     """
#     Extracts user data from the Telegram message and retrieves an existing TelegramUser from
#     the database based on the Telegram ID, or creates a new one if it doesn't exist.
#     """
#     from bot.models import TelegramUser
#
#     user_id = str(message.from_user.id)
#     first_name = message.from_user.first_name
#     last_name = message.from_user.last_name or ''
#     username = message.from_user.username or ''
#
#     user, created = TelegramUser.objects.get_or_create(
#         tg_id=user_id,
#         defaults={
#             'name': first_name,
#             'surname': last_name,
#             'tg_username': username
#         }
#     )
#     return user

