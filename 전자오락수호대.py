import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=637931&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") 

# 화면에 있는 전자오락수호대 제목과 링크 가져오가
제목들 = soup.find_all("td", attrs = {"class" : "title"}) # find_all을 사용해서 조건에 맞는 태그가 전부 다 배열형태로 나옴
# print(제목들[1].a.get_text(),)
# link = 제목들[1].a["href"]
# print("https://comic.naver.com" + link)

for 웹툰 in 제목들: 
    제목 = 웹툰.a.get_text()
    link = "https://comic.naver.com" + 웹툰.a["href"]
    print(제목, link)
#print(제목들)