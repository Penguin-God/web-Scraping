'''
[오늘의 날씨]
온도, 강수확률, 미세먼지 농도

[헤드라인 뉴스]
3개 제목 및 링크

[IT뉴스]
3개 제목 및 링크

[해커스 어학원 회화]
영어 회화
영어 회화 뜻풀이
'''

import requests
from bs4 import BeautifulSoup

def Creat_soup(url):    
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    res = requests.get(url, headers = head)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    return soup

def Weather():
    print("[오늘의 날씨]")
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=1&acr=1&acq=%EC%84%9C%EC%9A%B8+%EB%82%98&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    soup = Creat_soup(url)
    # 정보 가져오기
    today_Weather = soup.find("p", attrs = {"class" : "cast_txt"}).get_text()
    current_Temperature = soup.find("p", attrs = {"class" : "info_temperature"}).get_text().replace("도씨", "") # 도씨가 ℃랑 겹치니까 replace()로 빈칸으로 만듬
    min_Temperatuer = soup.find("span", attrs = {"class" : "min"}).get_text()
    max_Temperatuer = soup.find("span", attrs = {"class" : "max"}).get_text()
    rain_Percentage_Morning = soup.find("span", attrs = {"class" : "point_time morning"}).get_text().strip()
    rain_Percentage_After = soup.find("span", attrs = {"class" : "point_time afternoon"}).get_text().strip()
    미세먼지_농도 = soup.find("dl", attrs = {"class" : "indicator"}).find_all("dd")[0].get_text()
    초미세먼지_농도 = soup.find("dl", attrs = {"class" : "indicator"}).find_all("dd")[1].get_text()
    # soup.find("dl", attrs = {"class" : "indicator"}, text = "asd") text가 asd인 것을 가져옴 []로 감싸서 여러개 넣을 수 있음
    # 출력
    print(today_Weather)
    print("현재 온도 : {} (최저 {}/ 최고 {})".format(current_Temperature, min_Temperatuer, max_Temperatuer))
    print("오전 {} / 오후 {}".format(rain_Percentage_Morning, rain_Percentage_After))
    print("오늘의 미세먼지 농도 : {},   초미세먼지 농도 : {}".format(미세먼지_농도, 초미세먼지_농도))
    print()
    print()

def Headline_news():
    url = "https://news.naver.com/"
    soup = Creat_soup(url)
    print("[헤드라인 뉴스]")
    news_list = soup.find("ul", attrs = {"class" : "hdline_article_list"}).find_all("li", limit = 3) # find_all쓰고 find쓰면 안됨, limit : 찾는 개수 제한
    for i in range(len(news_list)):
        news_data = news_list[i].find("a")
        title = news_data.get_text().strip()
        link = news_data["href"]
        Print_news(i, title, "https://news.naver.com/" + link)  
    print()

def It_news():
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = Creat_soup(url)
    print("[IT뉴스]")
    news_list = soup.find("ul", attrs = {"class" : "type06_headline"}).find_all("li", limit = 3)
    for index, news_data in enumerate(news_list):
        img = news_data.find("img")
        a_index = 0
        if(img):
            a_index = 1
        title = news_data.find_all("a")[a_index].get_text().strip()
        link = news_data.find_all("a")[a_index]["href"]
        Print_news(index, title, link) 
    print()

def Print_news(index, title, link):
    print(str(index + 1) + "번째 기사")
    print(title)
    print(link)

def English_Proverb():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/B_others_wisesay&keywd=haceng_submain_lnb_eng_B_others_wisesay&logger_kw=haceng_submain_lnb_eng_B_others_wisesay#;'
    soup = Creat_soup(url)
    print("[해커스 어학원 회화]")
    en_Proverb = soup.find("div", attrs = {"class" : "text_en"}).find("p").get_text()
    ko_Proverb = soup.find("div", attrs = {"class" : "text_ko"}).find("p").get_text()
    print("(영어지문)")
    print(en_Proverb)
    print()
    print("(한글지문)")
    print(ko_Proverb)
    

if(__name__ == '__main__'):
    Weather() # 오늘의 날씨 가져오기
    Headline_news() # 네이버 해드라인 뉴스 3개 가져오기 
    It_news() # It뉴스 3개 가져오기
    English_Proverb() # 해커스 오늘의 영어 명언 가져오기
