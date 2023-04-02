from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging
from handlers1 import admin, callback, client, extra, fsm
from database.db import sql_create
async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0],
                          text="Бот запущен!")
    sql_create()

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)