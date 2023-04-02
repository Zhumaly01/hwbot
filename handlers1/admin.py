from aiogram import types, Dispatcher
from config import ADMINS, bot
from database.db import sql_command_all
async def bin_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:  # Закреплять сообщения могут только админы
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
    else:
        await message.answer('Пиши в группу')

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("ТЫ НЕ МОЙ БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

async def all_mentors(message: types.Message):
    mentors = await sql_command_all()
    for user in mentors:
        await message.answer(f"id: {user[0]}\n"
                             f"fullname:{user[1]}\n"
                             f"direction:{user[2]}\n"
                             f"age:{user[3]}\n"
                             f"gruppa:{user[4]}")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(bin_handler, commands=['bin'], commands_prefix='!/')
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(all_mentors, commands=["alm"])