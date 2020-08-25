import requests as rs
res = rs.get("https://www.naver.com/")
res.raise_for_status() #res.status_code가 정상이 아니면 에러냄
print("응답코드 : ", res.status_code) #200이면 정상