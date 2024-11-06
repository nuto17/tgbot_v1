import asyncpg
import asyncio
import psycopg2
from psycopg2 import sql

async def connect_db():
    conn=await asyncpg.connect(
        user = 'postgres',
        password='123',
        database='telega_nuto17',
        host = '127.0.0.1'
    )
    return conn

async def add_trata(amount, category, description, user_id):
    conn= await connect_db()
    await conn.execute('''
                       INSERT INTO expenses (amount, category, description, user_id) VALUES ($1,$2,$3,$4)
                       ''', amount, category, description, user_id)
    await conn.close()
    
    
#test
async def test_ex():
    await add_trata(500,'игры',"купил скин")
    print("Трата на месте")

if __name__=="__main__":
    asyncio.run(test_ex())
#test
   
#psql -U postgres -d telega_nuto17   

async def poluchit_rasxod(user_id):
    conn = await connect_db()
    rows = await conn.fetch(''' 
        SELECT amount, category, description, created_at
        FROM expenses
        WHERE user_id = $1
        ORDER BY created_at DESC
    ''', user_id)
    await conn.close()
    return rows
