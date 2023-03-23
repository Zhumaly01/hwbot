from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
help_button = KeyboardButton("/help")
mem_button = KeyboardButton("/mem")

share_location = KeyboardButton("Share Location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(
    start_button,
    quiz_button,
    help_button,
    share_location,
    share_contact,
    mem_button
)
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('ДА'),
    KeyboardButton('НЕТ')
)
cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)