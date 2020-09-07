import requests
from bs4 import BeautifulSoup



for year in range(2015, 2020):
    url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'.format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html5lib")
    images = soup.find_all("img", attrs = {"class" : "thumb_img"})

    for index, img in enumerate(images):
        if(index > 4): # 상위 5개의 영화 이미지만 가져오기
            break
        img_url = img["src"]
        if(img_url.startswith("//")): # img_url이 //으로 시작한다면
            img_url = "https:" + img_url
        print(img_url)
        
        # img_url 창의 정보를 가져오기
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("{}년_{}번째 영화.jpg".format(year, index + 1), "wb") as f:
            f.write(img_res.content) # img_res의 content정보를 파일로 쓰겠다.
