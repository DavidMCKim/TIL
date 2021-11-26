# 02_in.py

# in/ not in 연산자
# 문자열 in 변수명(문자열)
# 결과는 True / False

string = 'Python Programming'

if ('Python' in string) :
    print('있음')
else :
    print('앖음')

if 'thon'in string :
    print('있음')
else:
    print('앖음')

print('Python' not in 'Python programming')

# 아래와 같이 ID가 저장되어 있는 list 가 있다
ids = ['sun', 'flower', 'moon', 'sky']

# 사용자가 입력한 id가 list에 있으면 로그인 성공을 출력하고 없으면 로그인 실패라고 출력하시오.
id = input('ID 입력 :')

if id in ids :
    print('로그인 성공')
else :
    print('로그인 실패')