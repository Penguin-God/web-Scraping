# Headless Chrome : 웹 스크래핑 시 크롬창을 띄우지 않고 웹페이지 정보를 크롤링을 해 메모리 손해를 줄이고 더 빠르게 크롤링을 하는 방법
# 구글 플레이 무비 할인 영화 정보 가져오기
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import time

# headless chrome 설정하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # 안보이는 창의 크기를 몇으로 할건지 정의
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36") # headless chrome에서 useragent정의
browser = webdriver.Chrome("C:/Users/gkswh/OneDrive/바탕 화면/programmig language/파이썬/web-Scraping/Selenium/chromedriver.exe", options=options) # 노트북하고 데스크탑이랑 주소가 다름
browser.maximize_window()
url = "https://play.google.com/store/movies/top"
browser.get(url)

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
browser.get_screenshot_as_file("google_movie.png") # 다 끝나면 확인겸 스크린샷 찍음

# 뷰티불 수프로 정보 가져오기
soup = BeautifulSoup(browser.page_source, "html5lib")
Movies = soup.find_all("div", attrs = {"class" : ["Vpfmgd"]})
for Movie in Movies:
    Title = Movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text() 
    original_Price = Movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    if(original_Price):
        original_Price = original_Price.get_text()
        sale_Price = Movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
        Movie_link = Movie.find("a", attrs = {"class" : "JC71ub"})["href"]
        print(f"제목 : {Title}")
        print(f"할인전 금액 : {original_Price}")
        print(f"할인된 금액 : {sale_Price}")
        print("링크 : https://play.google.com" + Movie_link) 
        print('-' * 120, '\n')
browser.quit()