from database.connection import get_connection
import asyncpg

async def vvod_dannix(user_id,artist_name,popularity):
    conn = await get_connection()
    try:
        await conn.execute("SELECT 1")
        await conn.execute(
            """
            INSERT INTO spotify_top_artists (user_id, artist_name, popularity)
            VALUES ($1, $2, $3)
            """,
            user_id, artist_name, popularity
        )
    except Exception as e:
        print(f"ошибка ввода данных: {e}")
        await conn.rollback()
    finally:
        await conn.close()
        