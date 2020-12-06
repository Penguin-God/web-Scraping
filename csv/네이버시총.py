# 네이버 시총 1등부터 50등까지 가져옴
import csv
from bs4 import BeautifulSoup
import requests
import os

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' # 맨뒤에 원하는 페이지를 붙여서 가지고오기

filename = "시가총액-200등.csv"
script_dir = 'C:/Users/parkj/Desktop/프로그래밍/python/web-Scraping/csv'
abs_file_path = os.path.join(script_dir, filename)
f = open(abs_file_path, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 헤더 넣기
title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split("\t")
# tap으로 구분되어 있어서 split을 하면 ["N", "종목명"....]형식으로 된다
writer.writerow(title) # writerow : 행에 정보를 쓰는것인듯

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html5lib")

    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr") # talbe안의 tbody안의 모든tr을 가져옴
    for row in data_rows:
        colums = row.find_all("td") # 모든 td를 가져옴
        if(len(colums) <= 1):
            continue # 의미없는 데이터는 스킵
        data = [colum.get_text().strip() for colum in colums] # td안의 text를 가져옴
        writer.writerow(data) # csv file produce