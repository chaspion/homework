import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get("https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713", headers = headers)

soup = BeautifulSoup(data.text, 'html.parser')

allmusic = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in allmusic:
    name = music.select_one('td.info > a.title.ellipsis')
    if name is not None:
        name = ' '.join(name.text.split())
        rank = music.select_one('td.number').text.split()[0]
        artist = music.select_one('td.info > a.artist.ellipsis').text

        print(rank, name, artist)

    music_db = {
        'rank': rank,
        'title': name,
        'artist': artist
    }

    db.music.insert_one(music_db)
