#import matplotlib.pyplot as dig

#sync def create_diag(data,file_path='spotify_chart.png'):
    artists = [item['artist_name'] for item in data]
    popularities=[item['popularity'] for item in data]
    
    #построение диаграммы
    dig.figure(figsize=(7, 3))
    dig.bar(artists,popularities,color='purple')
    
    dig.xlabel('исполнители')
    dig.ylabel('популярность')
    dig.title('мой топ 5')
    dig.xticks(rotation=30, ha='center')
    
    dig.tight_layout()
    dig.savefig(file_path)
    dig.close()
    
    