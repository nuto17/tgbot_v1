from instagrapi import Client
import os
import logging
from dotenv import load_dotenv
load_dotenv()

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Путь к файлу с cookies
session_file_path = "instagram/session.json"
password= os.getenv('password_inst')

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
    client.login("nuto17_", "Semeniuta10")
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
    medias = client.collection_medias(selected_collection.id, amount=5)

    # Папка для сохранённых видео
    download_folder = "video"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Скачиваем рилсы из коллекции
    for media in medias:
        if media.media_type == 2:  # Тип 2 — это видео (включая рилсы)
            try:
                path = client.clip_download(media.pk, folder=download_folder)
                logging.info(f"Рилс скачан по пути: {path}")
            except Exception as e:
                logging.error(f"Ошибка при скачивании рилса: {e}")
