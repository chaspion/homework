import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
db.movies.remove

we_rating = db.movies.find_one({'title': '월-E'})
print(we_rating)

movies = db.movies.find({'rating': we_rating})
for movie in movies:
    db.users.update_many(movie['title'])

#
# # response_data = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")
# # city_air = response_data.json()
# #
# # rows =
# # print(city_air['RealtimeCityAir']['row'][0]['NO2'])



# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# for i in range(1, 11):
#     html = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716&page='+ str(i) , headers=headers)
#     # #
#     html_soup = BeautifulSoup(html.text, 'html.parser')
#     trs_soup = html_soup.select(('#old_content > table > tbody > tr'))
#
#     for tr_soup in trs_soup:
#         a = tr_soup.select_one("td.title > div > a")
#         if a is not None:
#             rank = tr_soup.select_one('td.ac > img')['alt']
#             title = a.text
#             point = tr_soup.select_one('td.point').text
#             print(rank, title, point)
#             doc = {
#                 'rank': rank,
#                 'title': title,
#                 'rating': point
#             }
#             db.movies.insert_one(doc)
        # same as db.movies.insert_one({'rank':rank}...)


# #
# # for tr in movies:
# #     title = tr.select_one('td.title > div > a')
# #     rating = tr.select_one('td.point')
# #     if title and rating is not None:
# #         print(title.text, rating.text)
#
# html = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers = headers)
#
# html_soup = BeautifulSoup(data.text, 'html.parser')
# trs = soup.select('#regularTeamRecordList_table > tr')
#
# for tr in trs:
#     rank = tr.select_one('th > strong')
#     name = tr.select_one('td.tm > div > span')
#     win_ratio = tr.select_one('td:nth-child(7) > strong')
#
#     if rank and name and win_ratio is not None:
#         print(rank.text, name.text, win_ratio.text)

#
# all_users = db.users.find({'age': 40})
# # for user in all_users:
# #     print(user['name'])
#
# user = db.users.find_one({'age': 40})
#
# same_ages = list(db.users.find({'age': 40}))
# for all_user in same_ages:
#     print(all_user)
#
# db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
#
# db.users.delete_one({'name': '론'})
#
# user = {'name': '론', 'age': 40}
# db.users.insert_one(user)