import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 웹사이트의 모든 정보를 가지고 있는 soup객체 생성
# print(soup.title) #웹사이트의 title 가져옴
# print(soup.title.get_text()) # title의 글자만 가져옴 
# print(soup.a) #가장먼저 발견되는 a 엘리먼트를 가지고 와라
# print(soup.a.attrs) # a태그의 속성 정보를 가지고 와라
# print(soup.a["href"]) # a태그의 href의 속성 '값' 정보를 가지고 와라
#print(soup.find("a", attrs = {"onclick" : "nclk_v2(event,'LNB.toon');"})) # onclick = nclk_v2(event,'LNB.toon');인 a 태그를 가져와라
#print(soup.find(attrs = {"onclick" : "nclk_v2(event,'LNB.toon');"})) # onclick = nclk_v2(event,'LNB.toon');인 어떤 태그를 가져와라

#네이버 웹툰 1위부터 5등까지 가져오기
#rank1 = soup.find("li", attrs = {"class" : "rank01"}) 
# rank2 = soup.find("li", attrs = {"class" : "rank02"})
# rank3 = soup.find("li", attrs = {"class" : "rank03"})
# rank4 = soup.find("li", attrs = {"class" : "rank04"})
# rank5 = soup.find("li", attrs = {"class" : "rank05"})
# print(rank1.a.get_text()) # rank1을 그대로 가져오면 정보가 너무 많아서 변수로 만든후에 원하는 정보만 가져오기
# print(rank2.a.get_text())
# print(rank3.a.get_text())
# print(rank4.a.get_text())
# print(rank5.a.get_text())

# 태그 위아래 가져오가
# rank2 = rank1.next_sibling.next_sibling # next_sibling은 다음 태그 중간에 줄바꿈이 있어서 두번 씀
# print(rank2.a.get_text())
# rankone = rank2.previous_sibling.previous_sibling # previous_sibling은 위에 태크
# print(rankone.a.get_text())
#print(rankone.parent) # .parent는 부모를 가져옴(rankone의 부모는 ol로 모든 순위를 담고있음)

# find를 사용해서 태그 위아래 가져오기
#rank2 = rank1.find_next_sibling("li") # 다음 태그중에 ()안에 조건에 일치하는 것 가져오기
#print(rank2.a.get_text())

#전체순위 가져오기
#ranks = rank1.find_next_siblings("li") # sibling뒤에 s를 붙여서 형제들을 가져옴 
#print(ranks)

webtoon = soup.find("a", text = "1초-76화") # find : 조건에 해당하는 첫번쨰 태그를 가져옴
print(webtoon)

