# 부동산 퀴즈 : 다음에서 송파 헬리오 시티의 매물정보를 가져오기
# 출력 결과 : 거래 : 전세, 면적 : 140/110, 가격 : 165,000, 동 : 111동, 층 : 고/35
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser") 

정보 = soup.find_all("div", attrs = {"class" : "txt_ac"})

# 내가 푼 풀이
순서 = []
for i in range(len(정보) + 1):
    if(i % 5 == 0 and i != 0):
        순서.append(i)

for i in 순서:
    print("거래 :", 정보[i - 5].get_text())
    print("면적 :", 정보[i - 4].get_text(), "(공급/전용)")
    print("가격 :", 정보[i - 3].get_text(), "(만원)")
    print("동 :", 정보[i - 2].get_text())
    print("층 :", 정보[i - 1].get_text())
    print("-------------------{}------------------".format(int(i / 5)), "\n",)


# 자식 찾는 코드
# for i in range(len(정보)):
#     if(정보[i].select('div > a') == []):
#         print(정보[i].get_text())
#     else:
#         # 가격 = 정보[i].select('div > a')
#         # print(가격["href"])
#         print("aa")

# asd = 정보[2].select('div > a')
# print(정보[2].get_text())


# 나도코딩님이 푼 풀이
data_rows = soup.find("table", attrs = {"class" : "tbl"}).find("tbody").find_all("tr") # talbe안의 tbody안의 tr들을 가져옴
for index, data in enumerate(data_rows): # enumerate : for문이 몇 번째 반복문인지 확인할 때 사용 (index에 순서가 data에 정보가 들어감)
    columns = data.find_all("td") # tr안의 td를 가져옴
    
    print(" ===========매물{}============".format(index + 1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text(), "(공급/전용)")
    print("가격 :", columns[2].get_text(), "(만원)")
    print("동 :", columns[3].get_text())
    print("층 :", columns[4].get_text())

