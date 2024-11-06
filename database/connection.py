import asyncpg

async def get_connection():
    conn = await asyncpg.connect(
        user="postgres",
        password="123",
        database="telega_nuto17",
        host="localhost",
        port="5432"
    )
    return conn