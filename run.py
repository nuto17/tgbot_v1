import hupper
import asyncio
import logging
from nuto_config.config import TOKEN
from aiogram import Bot, Dispatcher
from handlers.routers.main_router import router
from napominalka.phonofoe import proverka
from napominalka.check import check

# Создаём инстанс бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем главный роутер, который объединяет все хендлеры
dp.include_router(router)

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Основная функция для запуска бота
async def main():
    asyncio.create_task(proverka(bot))
    await dp.start_polling(bot)

# Запускаем бота с автообновлением (через hupper)
def run():
    asyncio.run(main())

if __name__ == '__main__':
    reloader = hupper.start_reloader('run.run')
    run()
