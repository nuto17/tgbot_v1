import asyncpg
import asyncio
async def get_connection():
    conn = await asyncpg.connect(
        user="postgres",
        password="123",
        database="nuto17base",
        host="localhost",
        port="5432"
    )
    return conn