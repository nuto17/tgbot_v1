from google.oauth2 import service_account
from googleapiclient.discovery import build 
import logging
import random
import io
from googleapiclient.http import MediaIoBaseDownload
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


service_account_file ='123/file with json/Reels from Nuto17bot.json'

SCOPES = ['https://www.googleapis.com/auth/drive']  # Права необходимые

creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

service = build('drive', 'v3',credentials=creds)

drive_folder_id = '17vhDSa2SEdnpQ5ZtDY_CxZAGAXfyA4qV'

def get_video():
    try:
        # Получаем список файлов
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)"
        ).execute()
        logging.info("успешно получил список файлов")
    except Exception as e:
        logging.error(f"ошибка {e}")
        return None

    # Проверяем, что есть файлы на диске
    items = results.get('files', [])
    if not items:
        logging.info("Диск пустой")
        return None
    else:
        # Выбираем случайный файл
        random_file = random.choice(items)
        file_id = random_file['id']
        file_name = random_file['name']
        logging.info(f"выбран случайный файл с id: {file_id} и name: {file_name}")

    # Скачиваем файл
    try:
        zapros = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        zagruzchik = MediaIoBaseDownload(fh, zapros)

        vipolneno = False
        while not vipolneno:
            status, vipolneno = zagruzchik.next_chunk()
            logging.info("Загрузка файла завершена")

        fh.seek(0)
        file_bytes = fh.read()
        logging.info("файл сохранен в память")
        return file_bytes

    except Exception as e:
        logging.error(f'ошибка {e}')
        return None
    
