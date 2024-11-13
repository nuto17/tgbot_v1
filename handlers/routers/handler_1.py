from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
import keyboards.keyboards as kd 
from huggingface_hub import InferenceClient
import os 
import logging
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

load_dotenv()

logging.basicConfig(level=logging.info)

api17=os.getenv('AI_API')

client = InferenceClient(api_key=api17)


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
        messages = [
            {
                "role": "user",
                "content": user_vopros
            }
        ]

        stream = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct",
            messages=messages,
            max_tokens=200,
            stream=True
        )

        response_text = ""
        for chunk in stream:
            response_text += chunk.choices[0].delta.content

        await message.answer(response_text,reply_markup=kd.vkluch)

    except Exception as e: 
        logging.error(f"ошибка {e}")
        await message.answer(f"произошла ошибка {e}")
        
    
    