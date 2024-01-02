import telebot
import os

from dotenv import load_dotenv
from film_retrieval.tmdb_api import get_movie_from_search
from film_retrieval.utils import format_movie_details, get_or_create_telegram_user
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

    # user = get_or_create_telegram_user(message)


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
    movie = get_movie_from_search(film_name)

    if movie:
        movie_details, keyboard = format_movie_details(movie)
        response_message = '\n'.join(movie_details)
        bot.send_message(message.chat.id, response_message, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't find any movies matching that name.")


@bot.callback_query_handler(func=lambda call: True)
def query_callback(call):
    movie_title = call.data
    movie = get_movie_from_search(movie_title)

    if movie:
        movie_details, keyboard = format_movie_details(movie)
        response_message = '\n'.join(movie_details)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=response_message,
                              reply_markup=keyboard)
    else:
        bot.answer_callback_query(call.id, "Sorry, I couldn't find any movies matching that name.")


bot.polling(none_stop=True)



