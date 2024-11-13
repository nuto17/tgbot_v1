from aiogram import Router
from handlers.routers import ai17, handler_1, handler_2, handler_3,magazin,napominalka,video_inst,ai17
# Регистрируем все хендлеры
router = Router()
handler_1.register(router)
handler_2.register(router)
handler_3.register(router)
#spotify_handler.register(router)
magazin.register(router)
napominalka.register(router)
video_inst.register(router)
ai17.register(router)


