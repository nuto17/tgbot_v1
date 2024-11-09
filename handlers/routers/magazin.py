from aiogram.types import Message,CallbackQuery,FSInputFile
from keyboards.keyboards import karti_magaz as kd
from aiogram.filters import Command

def register(router):
    @router.message(Command('karti'))
    async def otvet_karti(message: Message):
        await message.answer('Список карт',reply_markup=kd)
        
    @router.callback_query(lambda callback: callback.data == 'pyat')
    async def karta_5(callback: CallbackQuery):
        image=FSInputFile('/Users/nuto17/123/image_karti_magazinov/5terka.jpeg')
        await callback.message.answer_photo(image)
        await callback.answer()
        
    @router.callback_query(lambda callback: callback.data == 'magnit')
    async def karta_5(callback: CallbackQuery):
        image=FSInputFile('/Users/nuto17/123/image_karti_magazinov/magnit.jpeg')
        await callback.message.answer_photo(image)
        await callback.answer()

