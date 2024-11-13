from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from instagrapi import Client
import os
import logging
from dotenv import load_dotenv
from io import BytesIO
import concurrent.futures
import google.auth.exceptions
from tenacity import retry,stop_after_attempt,wait_fixed,retry_if_exception_type


# Загрузка переменных окружения
load_dotenv()

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Путь к файлу с cookies
session_file_path = "instagram/session.json"
password = os.getenv('password_inst')

client = Client()

# Проверяем, существует ли файл с cookies
if os.path.exists(session_file_path):
    try:
        # Загружаем cookies и пытаемся войти в аккаунт
        client.load_settings(session_file_path)
        client.login_by_sessionid("nuto17_")
        logging.info("Вход выполнен с использованием cookies.")
    except Exception as e:
        logging.error(f"Ошибка при входе с использованием cookies: {e}")
        # Если не получилось использовать cookies, нужно войти заново
        client.login("nuto17_", password)
        client.dump_settings(session_file_path)
        logging.info("Логин успешен и cookies сохранены.")
else:
    # Если cookies нет, выполняем стандартный вход
    client.login("nuto17_", password)
    client.dump_settings(session_file_path)
    logging.info("Логин успешен и cookies сохранены.")

# Получаем ID текущего пользователя
user_id = client.user_id_from_username('nuto17_')

# Получаем сохранённые медиа пользователя
collections1 = client.collections()

# Находим коллекцию "All Posts"
selected_collection = None
for collection in collections1:
    if collection.name == 'All posts':
        selected_collection = collection
        break

if selected_collection is None:
    logging.error("Коллекция 'All posts' не найдена.")
else:
    logging.info(f"Выбрана коллекция: '{selected_collection.name}'")

    # Получаем медиа из коллекции
    medias = client.collection_medias(selected_collection.id, amount=50)

    # Работа с Google Drive
    service_account_file = 'instagram/disk.json'

    SCOPES = ['https://www.googleapis.com/auth/drive']  # Права необходимые

    creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

    service = build('drive', 'v3', credentials=creds)

    drive_folder_id = '17vhDSa2SEdnpQ5ZtDY_CxZAGAXfyA4qV'

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5),retry=retry_if_exception_type(google.auth.exceptions.TransportError))
def skachka(media):
        if media.media_type == 2:
            try:
                reel_filename = f"{media.pk}.mp4"

                # Проверка наличия файла в Google Drive по названию
                query = f"name = '{reel_filename}' and '{drive_folder_id}' in parents"
                existing_files = service.files().list(q=query, fields="files(name)").execute()
                if existing_files.get('files'):
                    logging.info(f"Рилс {reel_filename} уже есть на диске.")
                    return
                
                # Скачиваем видео в байтовый объект
                reel_video = client.video_download(media.pk, folder="temp_downloads")
                with open(reel_video, "rb") as f:
                    file_bytes = BytesIO(f.read())
                
                # Загружаем видео на Google Drive
                file_metadata = {
                    'name': reel_filename,
                    'parents': [drive_folder_id]
                }

                media_body = MediaIoBaseUpload(file_bytes, mimetype='video/mp4')
                uploaded_file = service.files().create(
                    body=file_metadata,
                    media_body=media_body,
                    fields='id'
                ).execute()

                logging.info(f"Видео {media.pk} успешно загружено на Google Drive, ID: {uploaded_file.get('id')}")
                os.remove(reel_video)
            except Exception as e:
                logging.error(f"Ошибка при обработке видео {media.pk}: {e}")
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(skachka,medias)


