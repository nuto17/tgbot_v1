from aiogram.types import Message, FSInputFile,InputFile,BufferedInputFile
from googleapiclient.discovery import build
from google.oauth2 import service_account
from aiogram.filters import Command
from googleapiclient.http import MediaIoBaseDownload
import logging
from instagram.func_video import get_video
import io

service_account_file = 'instagram/disk.json'

SCOPES = ['https://www.googleapis.com/auth/drive']  # Права необходимые

creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

service = build('drive', 'v3', credentials=creds)

drive_folder_id = '17vhDSa2SEdnpQ5ZtDY_CxZAGAXfyA4qV'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def register(router):
    @router.message(Command('видео'))
    async def vidik(message: Message):
        video = get_video()
        video_file= BufferedInputFile(video, filename="random_video.mp4")
        try:
            await message.answer_video(video_file)
            logging.info("видео отправлено успешно")
        except Exception as e:
            logging.error(f"ошибка отправки: {e}")          