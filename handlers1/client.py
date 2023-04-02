from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards1.client_kb import start_markup
from wed import get_message


async def start_command(message: types.Message):
    await message.answer("Hello!", reply_markup=start_markup)



async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")


async def mem(message: types.Message):
    with open('media/img.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )
async def find(message: types.Message):
    await message.answer(get_message(message))
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(find,commands=['np'])