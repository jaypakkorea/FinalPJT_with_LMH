import requests
from bs4 import BeautifulSoup
from datetime import datetime

lanktoday = datetime.today().strftime('%Y%m%d')
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=${lanktoday}',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select("#old_content > table > tbody > tr")
movie_list=[]
for movie in movies:
    movie_name = movie.select_one("td.title > div > a")
    # movie_point = movie.select_one("td.point")
    if movie_name is not None:
        if len(movie_list)<10:
            if movie.select_one("td:nth-child(1) > img"):
                ranking = movie.select_one("td:nth-child(1) > img")["alt"]
                movie_list.append([int(ranking), movie_name.text])
            else:
                ranking = len(movie_list)
                movie_list.append([int(ranking), movie_name.text])
        else:break

# print(movie_list)


import os
import sys
import urllib.request
client_id = "zp580fkHgE57jjytcezD"
client_secret = "opbueu7dbW"
for movie in movie_list:
    encText = urllib.parse.quote(movie[1])
    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",'zp580fkHgE57jjytcezD')
    request.add_header("X-Naver-Client-Secret",'opbueu7dbW')
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)