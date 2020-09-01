import requests as rs
res = rs.get("https://www.google.com/")
res.raise_for_status() #res.status_code가 정상이 아니면 에러냄
print("응답코드 : ", res.status_code) #200이면 정상
print(len(res.text))
#print(res.text)

#with open("googleText.html", "w", encoding="utf8") as f:
#    f.write(res.text) #googleText.html 파일을 만든 후 f라고 이름 붙이고 ()안에 정보를 적는다