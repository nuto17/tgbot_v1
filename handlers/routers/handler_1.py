from aiogram.types import Message
from aiogram.filters import CommandStart
import keyboards.keyboards as kd 

# Функция для регистрации обработчиков в роутере
def register(router):
    @router.message(CommandStart())  # Хендлер для команды /start
    async def cmd_start(message: Message):
        await message.reply(
            f"Привет, гандон!\nТвой id ебанный: {message.from_user.id}\nИмя траханное: {message.from_user.first_name}",
            reply_markup=kd.main
        )