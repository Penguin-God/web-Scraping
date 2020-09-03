# 주소창에 page=숫자 의 형식을 바꾸면 원하는 page로 이동 가능
"""
우리가 웹페이지로 들어갈 때 서버에 요청을 보내고 서버는 그 요청에 맞게 응답을 해줌 이 요청중에 HTTP METHOD라는 것이 있음

HTTP METHID
1. Get방식 : 어떤 내용을 누구나 볼 수 있게 url에 적어서 보내는 방식
ex) https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000000&page=1 
?뒤에 변수와 값이 나옴 위에서는 최소최댓값 page변수와 값이 있음, 각 변수는 &로 구분함 
Get방식같은 경우는 내가 마음대로 값을 바꾸면서 쉽게 페이지 요청 가능
Get방식은 한번 보낼 수 있는 데이터 양에 한계가 있어서 큰 데이터 값은 보내지 않는다.

2. POST방식 : 보안정보와 같은 아무나 볼 수 없는 정보를 HTTP message body에 숨겨서 보내는 방식
페이지를 바꿨는데도 url정보가 같으면 POST방식을 사용한 것
"""

import requests 
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# 그냥 들어가니까 안됨 그래서 User Agent값을 넣어서 사람이 접속하는 것처럼 보이게 하는 코드를 작성함
User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get(url, headers = User_Agent_head)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html5lib")
items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")}) # search-product로 시작하는 class를 찾기 위해 정규식 개행 사용
# name = items[1].find("div" , attrs = {"class" : "name"}).get_text()
#print(name)

def 정보확인(상품정보):
    if(상품정보):
        상품정보 = 상품정보.get_text()
    else:
        상품정보 = "상품정보가 없습니다."
    return 상품정보

번수 = 1

def 정보출력():
    print(str(번수) + "번째" '\n'
    "이름 :",  name, '\n' 
    "가격 :",  Price, "  평점 :", 정보확인(평점), "  평점수 :", 정보확인(평점수), '\n')

for item in items:
    # 광고상품 제외
    광고상품 = item.find("span", attrs = {"class" : "ad-badge-text"})
    if(광고상품):
        print("<광고상품입니다.>" '\n')
        continue #다음반복문 실행

    # 리뷰 100개이상 평점 4.5점 이상만 불러오기

    name = item.find("div", attrs = {"class" : "name"}).get_text()
    Price = item.find("strong", attrs = {"class" : "price-value"}).get_text()
    평점 = item.find("em", attrs = {"class" : "rating"})
    평점 = 정보확인(평점)
    평점수 = item.find("span", attrs = {"class" : "rating-total-count"})
    평점수 = 정보확인(평점수) # (숫자)식으로 정보가 표기됨
    if(평점 == "상품정보가 없습니다." or 평점수 == "상품정보가 없습니다."):
        print("상품정보가 없습니다.")
        continue
    if(float(평점) >= 4.5 and int(평점수) >= 100):
        print(정보출력)
    #print("가격 :",  Price, "  평점 :", 평점, "  평점수 :", 평점수, '\n')
