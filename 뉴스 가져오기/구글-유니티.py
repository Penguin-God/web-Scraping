import requests 
import re
from bs4 import BeautifulSoup

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
url = "https://www.google.com/search?rlz=1C1OKWM_koKR907KR907&biw=1536&bih=775&tbm=nws&sxsrf=ALeKk01g441A_PGHxtl40r7dfIS7kYiFdg%3A1599214272495&ei=wBJSX5ztHdfWhwO814DYBw&q=%EC%9C%A0%EB%8B%88%ED%8B%B0&oq=%EC%9C%A0%EB%8B%88%ED%8B%B0&gs_l=psy-ab.3..0l10.5054.6825.0.7016.7.7.0.0.0.0.161.301.0j2.3.0....0...1c.1j4.64.psy-ab..4.2.300.0...112.XkKpIJ40TtY"
res = requests.get(url, headers = User_Agent_head)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html5lib")
news = soup.find_all("div", attrs = {"class" : "dbsr"})

번수 = 1
for 뉴스 in news:
    제목 = 뉴스.find("div", attrs = {"class" : "JheGif nDgy9d"}).get_text()
    link = 뉴스.find("a", {"style" : "text-decoration:none;display:block"})["href"]
    print(str(번수)+"번째 기사" '\n' , 제목, '\n', link)
    print("-" * 100, '\n')
    번수 += 1