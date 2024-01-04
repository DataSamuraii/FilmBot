from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


def create_rating_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("⭐️ 1", callback_data='rate_1'),
        InlineKeyboardButton("⭐️ 2", callback_data='rate_2'),
        InlineKeyboardButton("⭐️ 3", callback_data='rate_3'),
        InlineKeyboardButton("⭐️ 4", callback_data='rate_4'),
        InlineKeyboardButton("⭐️ 5", callback_data='rate_5')
    )
    return keyboard


def setup_preference_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    genres = ["Action", "Comedy", "Drama", "Fantasy", "Horror"]
    for genre in genres:
        keyboard.add(genre)
    return keyboard

