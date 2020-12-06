# 구글 플레이 무비 할인 영화 정보 가져오기
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time

User_Agent_head = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                    "Accept-Language" : "ko-KR,ko" 
# 페이지에 들어갈때 유저 에이전트에 따라 다른 정보를 주는 사이트가 있는데 이때 페이지를 그냥 크롤링하면 기본 언어인 영어를 가져오게 되는데
# 위의 랭귀지 코드를 작성해 원하는 언어의 정보를 크롤링하도록 함
}
url = "https://play.google.com/store/movies/top"
# HTML 확인하는 코드
# filename = "Movie.html"  
# script_dir = 'C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/Selenium'
# abs_file_path = os.path.join(script_dir, filename)
# with open(abs_file_path, "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # html코드를 예브게 써줌 

browser = webdriver.Chrome("C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/Selenium/chromedriver.exe") 
browser.maximize_window()
browser.get(url)
# 지정한 위치로 스크롤 내리기 
#browser.execute_script("window.scrollTo(0, 1080)") # 1080위치만큼 스크롤바를 내리는 코드 만약 0이면 맨위로 스크롤을 올림

#맨 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 현재 위치에서 맨아래로 스크롤을 내림
save_coordinate = browser.execute_script("return document.body.scrollHeight")  

while(True):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3) # 로딩 대기
    current_coordinate = browser.execute_script("return document.body.scrollHeight") # 현재 스크롤 위치 저장 
    if(save_coordinate == current_coordinate): 
        break # 위에서 스크롤을 내렸는데도 전에 위치와 똑같다면 더이상 내릴곳이 없다는 뜻이므로 break
    save_coordinate = current_coordinate # 값이 서로 다르면 갱신
print("스크롤 끗")

soup = BeautifulSoup(browser.page_source, "html5lib")
#Movies = soup.find_all("div", attrs = {"class" : ["ImZGtf mpg5gc", "Vpfmgd"]}) # 배열안에 있는 클래스들을 다 가져옴
Movies = soup.find_all("div", attrs = {"class" : ["Vpfmgd"]})
# print(len(Movies))
for Movie in Movies:
    Title = Movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text() 
    original_Price = Movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    if(original_Price):
        print(f"제목 : {Title}")
        original_Price = original_Price.get_text()
        print(f"할인전 금액 : {original_Price}")
        sale_Price = Movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
        print(f"할인된 금액 : {sale_Price}")
        Movie_link = Movie.find("a", attrs = {"class" : "JC71ub"})["href"]
        print("링크 : https://play.google.com" + Movie_link) 
        print('-' * 120, '\n')
browser.quit()