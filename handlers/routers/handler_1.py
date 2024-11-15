from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
import keyboards.keyboards as kd 
import requests
import os 
import logging
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

load_dotenv()

logging.basicConfig(level=logging.info)

class userstate(StatesGroup):
    main=State()
    ai_mode=State()

# Функция для регистрации обработчиков в роутере
def register(router):
    @router.message(CommandStart())  # Хендлер для команды /start
    async def cmd_start(message: Message,state: FSMContext):
        await state.set_state(userstate.main)
        await message.reply(
            f"привет! если хочешь активировать ai-mode, то нажми на него. Если ты хочешь работать с командами бота, то выбери 'команды' ",
            reply_markup=kd.ai_mode
        )
        
    @router.callback_query(lambda callback: callback.data == 'on')
    async def vkluchenie(callback: CallbackQuery,state: FSMContext):
        await state.set_state(userstate.ai_mode)
        await callback.answer("режим ai-mode включен")
        await callback.message.edit_reply_markup(reply_markup=kd.vkluch)    
        
    @router.callback_query(lambda callback: callback.data == 'off')
    async def vikluchenie(callback: CallbackQuery,state: FSMContext):
        await state.set_state(userstate.main)
        await callback.answer("режим ai-mode выключен")
        await callback.message.edit_reply_markup(reply_markup=kd.vikluch)
        
    @router.message(userstate.ai_mode)
    async def otpravka_voprosov(message:Message,state: FSMContext):
        await send_vopros(message)
    
    
    
async def send_vopros(message: Message):
    user_vopros=message.text
    try:
        prompt = {
    "modelUri": "gpt://b1gr568vlh0l85uak3os/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.5,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты разговорчивый и дружелюбный ассистент. Помогай, как хороший друг.Не используй специальные символы для выделения, такие как звездочки или подчеркивания.Общайся на ты.Сейчас 2024 год и ищи акутальную информацию."
        },
        {
            "role": "user",
            "text": "Как зовут Навального?"
        },
        {
            "role": "assistant",
            "text": "Алексей Навальный."
        },
        {
            "role": "user",
            "text": user_vopros
        },
    ]
        }
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

        headers={
        "Content-Type": "application/json",
        "Authorization": "APi-Key AQVNwjHkC2q66txhFSIzOSBpEYMlKnnDT2s3FlmW"
        }

        response=requests.post(url,headers=headers,json=prompt)
        if response.status_code==200:
            logging.info("успешно получил ответ")
            data=response.json()
            try:
                yan_response = data["result"]["alternatives"][0]["message"]["text"]
                await message.answer(yan_response)
            except (KeyError,IndexError) as e:
                logging.error(f"ошибка при извлечении текста: {e}")
                
                
    except Exception as e: 
        logging.error(f"ошибка {e}")
        await message.answer(f"произошла ошибка {e}")
        
    
    