import csv
from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' # 맨뒤에 원하는 페이지를 붙여서 가지고오기

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html5lib")

    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr") # talbe안의 tbody안의 모든tr을 가져옴
    for row in data_rows:
        colums = row.find_all("td") # 모든 td를 가져옴
        if(len(colums) <= 1):
            continue # 의미없는 데이터는 스킵
        data = [colum.get_text().strip() for colum in colums] # td안의 text를 가져옴
        print(data)