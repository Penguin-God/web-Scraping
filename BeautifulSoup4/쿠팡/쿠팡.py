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
soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")}) # search-product로 시작하는 class를 찾기 위해 정규식 개행 사용
name = items[1].find("div" , attrs = {"class" : "name"}).get_text()
print(name)
