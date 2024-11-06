from aiogram.types import Message
import random# Избегаем циклического импорта, импортируем router из общего файла
import keyboards.keyboards as kd # Импортируем клавиатуру # Импортируем фильтр F для фильтрации сообщений
# Функция для регистрации обработчика для команды 'сколько см?'
def register(router):
    @router.message(lambda message: message.text== 'сколько см?')
    async def skolko_sm(message: Message):
        sm = str(random.randint(1, 10))
        await message.answer(f"Твой член: {sm} см", reply_markup=kd.chelen)

# Комментарий: answer от reply отличается тем, что reply именно ответ на сообщение, а answer отправляет обычное сообщение.
