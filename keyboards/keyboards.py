from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='погода' )],
    [KeyboardButton(text='расходы')],
    
],          resize_keyboard=True,
            input_field_placeholder="Выбери длину члена"
                           )
dreamcar=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Porsche',url='https://www.youtube.com/watch?v=Dt-0NVt6jSw',callback_data='911')],
    [InlineKeyboardButton(text='BMW',url='https://www.youtube.com/watch?v=RurHZGQtbmg',callback_data='m8')]

])
chelen = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "хочешь увеличить член?", url = 'https://www.youtube.com/watch?v=vQC8jHwl6eY')]
])
week = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать день: ', callback_data='day')]
])
raspisanie= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='monday', callback_data='pon')],
    [InlineKeyboardButton(text='thuesday', callback_data='vtor')],
    [InlineKeyboardButton(text='wend', callback_data='sred')],
    [InlineKeyboardButton(text='saturday', callback_data='chet')],
    [InlineKeyboardButton(text='friday', callback_data='pyat')],
    [InlineKeyboardButton(text='thursday', callback_data='sub')]

])
cars = ['Porsche','BMW']
#ассинхрон для того чтобы машины выдавало значения в кнопку клавы
async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        if car=='Porsche':
            url='https://www.youtube.com/watch?v=Dt-0NVt6jSw'
        else:
            url='https://www.youtube.com/watch?v=RurHZGQtbmg'
            
        keyboard.add(InlineKeyboardButton(text=car, url=url ))
    return keyboard.adjust(2).as_markup()

klavaweather= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Москва', callback_data='msk')],
    [InlineKeyboardButton(text='Казань',callback_data='kzn')],
    [InlineKeyboardButton(text='Северодвинск',callback_data='svd')]
])
funcrasxod=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='добавить')],
    #[KeyboardButton(text='убрать')],
    [KeyboardButton(text='просмотреть')]
])
karti_magaz=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='пятерочка',callback_data='pyat')],
    [InlineKeyboardButton(text='магнит',callback_data='magnit')]
])
ai_mode=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Включить Ai-mode", callback_data='on')],
    [InlineKeyboardButton(text="Оставить команды бота",callback_data='off')]
])
vkluch=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="выключить",callback_data='off')]
])
vikluch=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="включить",callback_data='on')]
])