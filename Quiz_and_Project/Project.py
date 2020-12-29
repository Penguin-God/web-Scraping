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




def Weather():
    print("[오늘의 날씨]")
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.asiw&fbm=1&acr=1&acq=%EC%84%9C%EC%9A%B8+%EB%82%98&qdt=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    # 정보 가져오기
    today_Weather = soup.find("p", attrs = {"class" : "cast_txt"}).get_text()
    current_Temperature = soup.find("p", attrs = {"class" : "info_temperature"}).get_text().replace("도씨", "") # 도씨가 ℃랑 겹치니까 replace()로 빈칸으로 만듬
    min_Temperatuer = today_Weather = soup.find("span", attrs = {"class" : "min"}).get_text()
    max_Temperatuer = today_Weather = soup.find("span", attrs = {"class" : "max"}).get_text()
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

if(__name__ == '__main__'):
    Weather()