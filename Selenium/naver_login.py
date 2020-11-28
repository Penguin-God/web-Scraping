from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
browser = webdriver.Chrome("C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/Selenium/chromedriver.exe") 
browser.get("https://naver.com")

# 로그인버튼 클릭
login = browser.find_element_by_class_name("link_login")
login.click()
# 로그인 우회
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "gkswh4860", pw = "2134okok^^") # 아이디 비번 입력
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()
