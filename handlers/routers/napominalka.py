from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from database.connection import get_connection
import asyncpg
import dateparser
from babel.dates import format_datetime
import random
from napominalka.emodji import emoji

class napominalka(StatesGroup):
    description = State()
    vremya=State()
    
def register(router):
    @router.message(Command('напомни'))
    async def dobavit(message: Message, state:FSMContext):
        await message.answer("о чем напомнить?")
        await state.set_state(napominalka.description)
    
    @router.message(napominalka.description)
    async def dobavit_vremya(message: Message, state: FSMContext):
        await state.update_data(description=message.text)
        await message.answer("когда напомнить?")
        await state.set_state(napominalka.vremya)
        
    @router.message(napominalka.vremya)
    async def vremyacheck(message:Message, state: FSMContext):
        user_data= await state.get_data()
        description=user_data['description']
        
        norm_vremya=dateparser.parse(message.text,settings={'PREFER_DATES_FROM': 'future'})
        if not norm_vremya:
            await message.answer("неверный формат ввода времени")
            return
        vremya= norm_vremya
        try:
            conn= await get_connection()
            async with conn.transaction():
                await conn.execute(
                    "INSERT INTO reminders (user_id, description, due_date) VALUES ($1, $2, $3)",
                    message.from_user.id, description, vremya
                )
        except asyncpg.PostgresError as e:
            await message.answer(f"произошла ошибка: '{e}'")
        finally:
            await conn.close()
        
        krasivoe_vremya=format_datetime(vremya, "d MMMM yyyy 'года' в HH:mm",locale='ru')
        smail=random.choice(emoji)
        
        await message.answer(f"напоминалка о {description} на {krasivoe_vremya} поставлена!{smail}")
        await state.clear()
