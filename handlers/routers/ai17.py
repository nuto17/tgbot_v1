import logging 
from aiogram.filters import Command
from aiogram.types import Message
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)

api17=os.getenv('AI_API')

client = InferenceClient(api_key=api17)

def register(router):
    @router.message(Command('вопрос'))
    async def send_vopros(message: Message):
        user_vopros=message.text[len('/вопрос'):]
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

            await message.answer(response_text)

        except Exception as e: 
            logging.error(f"ошибка {e}")
            await message.answer(f"произошла ошибка {e}")
        