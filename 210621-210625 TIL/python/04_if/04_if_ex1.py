# 다음과 같이 로그인 프로그램 작성

# 등록된 ID : flower
# 비밀번호 : 1234

ID = 'flower'
PW = '1234'

i = input("아이디 입력 : ")
p = input("비밀번호 입력 : ")

if ((i == ID) and (p == PW)) :
    print("로그인 성공!")
else :
    print("로그인 실패!")