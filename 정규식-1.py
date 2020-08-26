#정규식 : 말 그대로 정해진 식 ex) 주민등록번호, IP주소, 이메일, 학년반번호
import re #정규식 라이브러리
p = re.compile("ca.e") #()안에 것을 컴파일, . : 어떤 문자하나, ^ : 문자열의 시작을 의미 (^de) : de로 시작하는 것, $ : 문자열의 끝을 의미

def 매치프린트(매치값):
    if(매치값):
        print(매치값.group()) # 매칭된 값을 출력, 값이 매치되지 않으면 에러가 발생 위에"casse"라고 넣으면 에러뜸
        print(매치값.string) # 입력받은 문자열 출력
        print(매치값.start()) # 일치하는 문자열의 시작 index 출력 
        print(매치값.end())  # 일치하는 문자열의 끝 index 출력
        print(매치값.span()) # 일치하는 문자열릐 시작, 끝 index 출력
    else:
        print("매치되지 않음")

m = p.match("careless and asd") # match : 주어진 문자열의 처음부터 일치하는지 확인
#매치프린트(m)

s = p.search("please funking AD carry care") #search : 주어진 문자열 중에 일치하는게 있는지 확인
#매치프린트(s)

f = p.findall("careless and cafe, case") # findall : 일치하는 모든것을 리스트 형태로 가져옴
print(f, f[1])

'''
re.compile("원하는 형태") : 원하는 형태로 컴파일
.macth :  주어진 문자열의 처음부터 일치하는지 확인
.search : 주어진 문자열 중에 일치하는게 있는지 확인
.findall : 일치하는 모든것을 리스트 형태로 가져옴

원하는 형태 : 정규식
. : 어떤 문자하나
^ : 문자열의 시작 (^de) : de로 시작하는 것
$ : 문자열의 끝
'''