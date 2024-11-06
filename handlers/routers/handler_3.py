from aiogram.types import Message
import random  # Импортируем фильтр F для фильтрации сообщений

# Функция для регистрации обработчика для команды 'сколько iq?'
def register(router):
    @router.message(lambda message: message.text == 'сколько iq?')
    async def how_many_iq(message: Message):
        chisl_iq = str(random.randint(1, 100))
        await message.answer(f"Ваш IQ: {chisl_iq}")

# Комментарий: этот хендлер отвечает на запрос пользователя по тексту 'сколько iq?' и отправляет случайное значение IQ.
