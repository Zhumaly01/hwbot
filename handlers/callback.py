from config import bot,dp
from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("next", callback_data="button_2")
    markup.add(button_2)

    question = "Сколько яблок на березе??"
    answer = [
        "12",
        "3",
        "БЕССКОНЕЧНОСТЬ",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_3 = InlineKeyboardButton("next", callback_data="button_3")
    markup.add(button_3)

    question = "кто начал войну?"
    answer = [
        "Россия",
        "Украина",
        "АКШ",
        "Кыргызстан",
        "НАто",
        "Индусы",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=5,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )

async def quiz_4(call: types.CallbackQuery):
    question = "your mom know what are you gay?"
    answer = [
        "no",
        "yes",
        "what",
        "еше нет",
        "может быть",
        "Индусы",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="было очевидно",
        open_period=10,
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
    dp.register_callback_query_handler(quiz_4, text="button_3")