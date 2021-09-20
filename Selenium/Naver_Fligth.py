from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/Selenium/chromedriver.exe") 
browser.maximize_window() # 창 전체화면화
url = "https://flight.naver.com/flights/"
browser.get(url)

def AirFly(start_filed, end_filed, start_day, end_day):
    browser.find_element_by_link_text("인천").click()
    browser.find_elements_by_link_text(start_filed)[0].click() # [0] -> 이번달 
    browser.find_element_by_link_text("도착").click()
    browser.find_elements_by_link_text(end_filed)[0].click() # [0] -> 이번달
    # find_elements를 사용하면 여러개의 엘리먼트 정보를 가져올 수 있음

    browser.find_element_by_link_text("가는날 선택").click()
    browser.find_elements_by_link_text(start_day)[0].click() # [0] -> 이번달
    browser.find_elements_by_link_text(end_day)[1].click() # [1] -> 다음달

    browser.find_element_by_xpath("//*[@id='searchArea']/a").click()
    try:
        air_information = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) # 튜플 형태로 값을 보냄
        print(air_information.text)
    finally:
        browser.quit()

AirFly("제주", "광주", "30", "2")