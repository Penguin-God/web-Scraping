from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/Selenium/chromedriver.exe") 
browser.get("https://naver.com")
# 네이버 로그인창 클릭하는 코드
login = browser.find_element_by_class_name("link_login")
login.click()
# 로그인창에서 뒤로가기 한 후 검색창에 원하는 검색어를 입력후 검색하는 코드
browser.back()
search = browser.find_element_by_id("query")
search.send_keys("유나이트 서울 2020")
search.send_keys(Keys.ENTER)
# 현재부라우저의 a태의 href정보 가져오기
tag_a = browser.find_elements_by_tag_name("a")
for a in tag_a:
    a.get_attribute("href")