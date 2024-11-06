import asyncio
from aiogram import Bot
from napominalka.check import check

async def proverka(bot:Bot):
    while True:
        await check(bot)
        await asyncio.sleep(60)
           