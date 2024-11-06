from datetime import datetime
from database.connection import get_connection
from aiogram import Bot

async def check(bot: Bot):
    now=datetime.now()
    conn = await get_connection()
    
    reminders= await conn.fetch(
        "SELECT * FROM reminders WHERE due_date <= $1 AND notified = FALSE",
        now
    )
    
        # Отправляем напоминания и обновляем статус
    for reminder in reminders:
        user_id=reminder['user_id']
        description=reminder['description']
        await bot.send_message(user_id,f"смотри: {description}")
        
        #обновляю статус напоминалки
        await conn.execute(
            "UPDATE reminders SET notified = TRUE WHERE id = $1",
            reminder['id']
        )
        await conn.close()