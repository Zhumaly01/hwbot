from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from config import ADMINS
from keyboards1.client_kb import cancel_markup, submit_markup, start_markup
# from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    ID = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не админ!")# Закреплять сообщения могут только админы

    else:
        await FSMAdmin.ID.set()
        await message.answer('ID ментора ?')

async def load_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['ID'] = message.text
    await FSMAdmin.next()
    await message.answer("Имя ментора ?",reply_markup=cancel_markup)

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какая направление?")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?")

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")

    else:
        async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
            FSMCONTEXT_PROXY_STORAGE['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какая группа?")

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXT_PROXY_STORAGE:
        FSMCONTEXT_PROXY_STORAGE['group'] = message.text
        await message.answer(f'Инфа ментора:\n'
                             f'ID ментора - {FSMCONTEXT_PROXY_STORAGE["ID"]}\n'
                             f'имя ментора - {FSMCONTEXT_PROXY_STORAGE["name"]}\n'
                             f'направление - {FSMCONTEXT_PROXY_STORAGE["direction"]}\n'
                             f'возраст - {FSMCONTEXT_PROXY_STORAGE["age"]}\n'
                             f'группа - {FSMCONTEXT_PROXY_STORAGE["group"]}\n')
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=submit_markup)





async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        # await sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган!", reply_markup=start_markup)
    elif message.text == "НЕТ":
        await state.finish()
        await message.answer("Ну и пошел ты!", reply_markup=start_markup)
    else:
        await message.answer("Нормально пиши!", reply_markup=start_markup)


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_ID, state=FSMAdmin.ID)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)