import sqlite3
import datetime


def create_table():
    # создание бд
    with sqlite3.connect("news_bd.db") as db:
        cursor = db.cursor()

        # создание таблицы
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT,
        title TEXT
        );""")
        db.commit()