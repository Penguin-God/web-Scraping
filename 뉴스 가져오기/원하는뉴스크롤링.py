import requests 
import re
from bs4 import BeautifulSoup

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def 기사크롤링(검색, page):
    start = 0
    for i in range(1, page+1):
        # start = 0은 1page 10은 2page 20은 3page임
        url = 'https://www.google.com/search?q={}&tbm=nws&sxsrf=ALeKk00eYvpMb2KpkXuMYyGj3sV7U62eYA:1599278706082&ei=cg5TX67WBMSchwO2l66gCQ&start={}&sa=N&ved=0ahUKEwiu17C5kdHrAhVEzmEKHbaLC5Q4FBDy0wMIhQE&biw=1745&bih=881&dpr=1.1'.format(검색, start)
        res = requests.get(url, headers = User_Agent_head)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html5lib")
        news = soup.find_all("div", attrs = {"class" : "dbsr"})
        start += 10
        print(i, "page" '\n')

        번수 = 1
        for 뉴스 in news:
            제목 = 뉴스.find("div", attrs = {"class" : "JheGif nDgy9d"}).get_text()
            link = 뉴스.find("a", {"style" : "text-decoration:none;display:block"})["href"]
            print(str(번수)+"번째 기사" '\n' , 제목, '\n', link)
            print("-" * 100, '\n')
            번수 += 1

기사크롤링('카카오게임즈', 2)