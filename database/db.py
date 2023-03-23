from aiogram import types, Dispatcher
import sqlite3
#=====================================================================================================================

db = sqlite3.connect("database/bot.sqlite3")
cursor = db.cursor()

#=====================================================================================================================

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")
        db.execute("CREATE TABLE IF NOT EXISTS mentors "
                   "(id INTEGER PRIMARY KEY, "
                   "fullname VARCHAR (255), "
                   "direction VARCHAR(255), "
                   "age INTEGER, "
                   "grupa VARCHAR(255))")

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors "
                       "(id, fullname, direction, age, grupa) VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()