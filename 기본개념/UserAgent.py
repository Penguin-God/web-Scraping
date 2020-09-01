import requests as rs
url = "http://nadocoding.tistory.com"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"} # Key값은 내 useragent정보
res = rs.get(url, headers = head) #다른 사이트처럼 그냥 주소 쓰면 웹사이트에서 막아서 정보가 안 가져와짐
print("응답코드 : ", res.status_code) #200이면 정상
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text) 