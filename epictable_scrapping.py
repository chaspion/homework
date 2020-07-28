import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver

client = MongoClient('localhost', 27017)
db = client.dbsparta

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# data = requests.get("http://df.nexon.com/df/info/equipment/view?id=v1czui", headers = headers)

driver = webdriver.Chrome('C:/Users/YH/Documents/chromedriver.exe')
driver.get('https://dnf.akaib.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

epics = soup.select('#recent-epic > div > ul > li')

for epic in epics:
    time = epic.select_one('span.label.label-primary.pull-left')
    name = epic.select_one('span:nth-child(2) > b > a')
    channel = epic.select_one('span:nth-child(2) > i')

    if time and name and channel is not None:
        print(time.text, name.text, channel.text)
