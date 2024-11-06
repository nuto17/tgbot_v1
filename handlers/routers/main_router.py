from aiogram import Router
from handlers.routers import handler_1, handler_2, handler_3,magazin,napominalka
# Регистрируем все хендлеры
router = Router()
handler_1.register(router)
handler_2.register(router)
handler_3.register(router)
#spotify_handler.register(router)
magazin.register(router)
napominalka.register(router)




