#from aiogram.types import Message
#from aiogram.filters import CommandStart, Command
#from spotify.spot_func import sp
#from database.spotify_queris import vvod_dannix
#from spotify.diagram import create_diag
#from aiogram.types import FSInputFile

#def register(router):
    #@router.message(Command('spotify'))
    #sync def get_spoti(message: Message):
        user_id=message.from_user.id
        results= sp.current_user_top_artists(limit=5, time_range='short_term')
        
        #сохраняем в бд
        #for artist in results['items']:
            artist_name=artist['name']
            popularity=artist['popularity']
            #await vvod_dannix(user_id,artist_name,popularity)
        #await message.answer('данные закинуты в бд')
        
        data=[{'artist_name': artist['name'], 'popularity':artist['popularity']} for artist in results['items']]
        #await create_diag(data,'spotify_chart.png')
        
        photka_diagi=FSInputFile('spotify_chart.png')
        #await message.answer_photo(photka_diagi, caption='твоя диаграмма')
    