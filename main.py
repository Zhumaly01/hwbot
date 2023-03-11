from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")

@dp.message_handler(commands=["mem"])
async def mem(message: types.Message):
    with open('media/img.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text="button_1")
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
@dp.callback_query_handler(text="button_2")
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

@dp.callback_query_handler(text="button_3")
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
@dp.message_handler()
async def echo(message: types.Message):
    times = message.text
    if message.text == "python":
        await message.answer("I love it!")
    elif message.text.isdigit:
        await bot.send_message(message.from_user.id,int(message.text)**2)
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Салалекум хозяин {message.from_user.full_name}"
        )
        await message.answer(f"This is an answer method! {message.message_id}")
        await message.reply("This is a reply method!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)