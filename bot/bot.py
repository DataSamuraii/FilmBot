import telebot
import os

from dotenv import load_dotenv
from film_retrieval.tmdb_api import get_film_from_search
from film_retrieval.utils import format_film_details, create_telegram_user, create_film
from keyboards.keyboard import create_rating_keyboard
# TODO implement /search_by_actor and /search_by_genre


load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_API_TOKEN'))
print('FilmBot is running')


@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_message = (
        "🎬 Welcome to the Film Recommendation Bot! 🎬\n\n"
        "I can help you find movie recommendations based on your preferences. "
        "Just tell me a movie you like, and I'll do the rest!\n\n"
        "For more assistance, type /help."
    )
    bot.reply_to(message, welcome_message)

    create_telegram_user(message)


@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "💡 How to use this bot 💡\n\n"
        "1. Send me the name of a film, and I'll suggest something similar.\n\n"
        "If you have any questions or feedback, contact developer here: https://t.me/rubiick"
    )
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    film_name = message.text
    process_and_respond_film(message.chat.id, film_name)


@bot.callback_query_handler(func=lambda call: call.data.startswith('rec_'))
def query_callback(call):
    film_title = call.data.split('_')[1]
    process_and_respond_film(call.message.chat.id, film_title)


def process_and_respond_film(chat_id, film_title):
    film = get_film_from_search(film_title)

    if film:
        film_details, keyboard = format_film_details(film)
        response_message = '\n'.join(film_details)
        bot.send_message(chat_id, response_message, reply_markup=keyboard)

        film_response, error = create_film(film)
        if error:
            print(f"Error saving film: {error}")

        rating_message = 'If you have watched the film, please choose a rating.'
        rating_keyboard = create_rating_keyboard()
        bot.send_message(chat_id, rating_message, reply_markup=rating_keyboard)
    else:
        bot.send_message(chat_id, "Sorry, I couldn't find any films matching that name.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('rate_'))
def rating_callback(call):
    rating = int(call.data.split('_')[1])
    if 1 <= rating <= 5:
        bot.answer_callback_query(call.id, text=f"Thanks for rating {rating} stars!")
    else:
        bot.answer_callback_query(call.id, text="Invalid rating.")


bot.polling(none_stop=True)
