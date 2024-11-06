import asyncpg
import asyncio
from database.connection import get_connection

async def create_database_and_table():
    # Подключение к базе данных Postgres
    conn = await asyncpg.connect(user='postgres', password='123', host='127.0.0.1', port='5432', database='postgres')

    # Создание базы данных (если она еще не создана)
    try:
        await conn.execute('''
            CREATE DATABASE nuto17base;
        ''')
        print("База данных 'nuto17base' успешно создана.")
    except asyncpg.exceptions.DuplicateDatabaseError:
        print("База данных 'nuto17base' уже существует, пропускаем создание.")

    await conn.close()

    # Подключаемся к новой базе данных и создаем таблицу
    conn = await asyncpg.connect(user='postgres', password='123', host='127.0.0.1', port='5432', database='nuto17base')

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            description TEXT NOT NULL,
            due_date TIMESTAMP NOT NULL,
            notified BOOLEAN DEFAULT FALSE
        );
    ''')

    print("Таблица 'reminders' успешно создана.")
    await conn.close()

asyncio.run(create_database_and_table())
