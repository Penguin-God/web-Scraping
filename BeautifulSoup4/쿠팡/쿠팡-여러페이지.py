import requests 
import re
from bs4 import BeautifulSoup

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def 정보확인(상품정보):
    if(상품정보):
        상품정보 = 상품정보.get_text()
        if("(" in 상품정보):
            상품정보 = 상품정보[1:-1] # (13)식으로 출력되므로 0번째와 맨 마지막에 ()를 제외함 
    else:
        상품정보 = "상품정보가 없습니다."
    return 상품정보



def 정보출력():
    return print(str(i) + "페이지 :", str(번수) + "번째" '\n' "이름 :",  name, '\n' "가격 :",  Price, "  평점 :", 평점, "  리뷰수 :", 리뷰수)

번수 = 1
for i in range(1, 6):
    #print(str(i) + "페이지 :", str(번수) + "번째" )
    # .format()으로 page={} 부분에 i를 집어넣음
    # .format(asd) : {}안에 asd를 넣음
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
    res = requests.get(url, headers = User_Agent_head)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html5lib")
    items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")}) # search-product로 시작하는 class를 찾기 위해 정규식 개행 사용

    for item in items:
        # 광고상품 제외
        광고상품 = item.find("span", attrs = {"class" : "ad-badge-text"})
        if(광고상품):
            continue #다음반복문 실행

        name = item.find("div", attrs = {"class" : "name"}).get_text()
        Price = item.find("strong", attrs = {"class" : "price-value"}).get_text()
        평점 = item.find("em", attrs = {"class" : "rating"})
        평점 = 정보확인(평점)
        리뷰수 = item.find("span", attrs = {"class" : "rating-total-count"})
        리뷰수 = 정보확인(리뷰수) 
        
        if(평점 == "상품정보가 없습니다." or 리뷰수 == "상품정보가 없습니다."):
            continue
        
        link = item.find("a", attrs = {"class" : "search-product-link"})["href"]

        if(float(평점) >= 4.5 and int(리뷰수) >= 50 and "LG" in name):
            정보출력()
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-" * 100 , '\n')
            번수 += 1