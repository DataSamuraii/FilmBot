from telebot import types


def format_movie_details(movie):
    details = [
        f"🎬 Title: {movie['title']}",
        f"📅 Release Date: {movie['release_date']}",
        f"🌍 Country: {movie['country']}",
        f"🎭 Genre: {movie['genre']}",
        f"🌟 Cast: {movie['actors']}",
        f"🔞 Age Limit: {movie['age_limit']}",
    ]
    if movie.get('poster'):
        details.append(f"🖼️ Poster: {movie['poster']}")
    if movie.get('movies_to_recommend'):
        details.append(f"\n\n🔎You might also enjoy: {', '.join(movie['movies_to_recommend'])}")

        keyboard = types.InlineKeyboardMarkup()
        for title in movie['movies_to_recommend']:
            callback_button = types.InlineKeyboardButton(text=title, callback_data=title)
            keyboard.add(callback_button)
        return details, keyboard
    return details, None


def get_or_create_telegram_user(message):
    """
    Extracts user data from the Telegram message and retrieves an existing TelegramUser from
    the database based on the Telegram ID, or creates a new one if it doesn't exist.
    """
    from bot.models import TelegramUser

    user_id = str(message.from_user.id)
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ''
    username = message.from_user.username or ''

    user, created = TelegramUser.objects.get_or_create(
        tg_id=user_id,
        defaults={
            'name': first_name,
            'surname': last_name,
            'tg_username': username
        }
    )
    return user

