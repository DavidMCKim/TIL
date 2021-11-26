# 121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라. **
print('121')
i = input()
if i == i.upper() :
    i = i.lower()
else :
    i = i.upper()
############################################
# user = input("")
# if user.islower():
#     print(user.upper())
# else:
#     print(user.lower())
print("---------------------------------")
print()

# 122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수        학점
# 81~100    A
# 61~80     B
# 41~60     C
# 21~40     D
# 0~20      E
print('122')
scores = eval(input("당신의 점수를 입력하세요 : "))
if scores >= 81 :
    print("grade is A")
elif scores >= 61 :
    print("grade is B")
elif scores >= 41 :
    print("grade is C")
elif scores >= 21 :
    print("grade is D")
else :
    print("grade is E")
print("---------------------------------")
print()


# 123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. **
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 통화명       환율
# 달러        1167
# 엔         1,096
# 유로        1268
# 위안        171
print('123')
환율 = {"달러": 1167,
        "엔": 1.096,
        "유로": 1268,
        "위안": 171}
won = (input('입력: '))
num, currency = won.split(' ')
print(float(num) * 환율[currency], "원")
print("---------------------------------")
print()

# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
print('124')
num1 = eval(input('input number1: '))
num2 = eval(input('input number2: '))
num3 = eval(input('input number3: '))
if num1 >= num2 :
    if num1 >= num3 :
        print(num1)
    else :
        print(num3)
elif num2 >= num3 :
    print(num2)
else :
    print(num3)
print("---------------------------------")
print()

# 125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호        통신사
# 011        SKT
# 016        KT
# 019        LGU
# 010        알수없음
print('125')
num = input('휴대전화 번호 입력: ')
a,b,c=num.split('-')
if a == '011' :
    print('당신은 SKT 사용자입니다.')
elif a == '016' :
    print('당신은 KT 사용자입니다.')
elif a == '019' :
    print('당신은 LGU 사용자입니다.')
elif a == '010' :
    print('없는 번호 입니다.')
print("---------------------------------")
print()

# 126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다. **
#       0       1       2       3       4       5       6       7       8       9
# 01    강북구   강북구   강북구     도봉구   도봉구    도봉구    노원구   노원구    노원구    노원구
print('126')
i = input('우편번호: ')
i = i[:3]
if i in ['010', '011', '012'] :
    print('강북구')
elif i in ['013', '014', '015'] :
    print('도봉구')
else :
    print('노원구')

# x = i[3]
# if x < 3:
#     print('강북구')
# elif x < 6 :
#     print('도봉구')
# elif x < 10 :
#     print('노원구')
# else :
#     print('잘못된 우편번호입니다.')
print("---------------------------------")
print()

# 127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
print('127')
id = input('주민등록번호: ')
day, iden = id.split('-')
if iden[0] == '1' or iden[0] == '3' :
    print('남자')
else :
    print('여자')
print("---------------------------------")
print()

# 128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드      출생지
# 00~08       서울
# 09~12       부산
print('128')
for i in range(2) :
    id = input('주민등록번호: ')
    day, iden = id.split('-')
    d = iden[1:3]
    d= int(d)
    if  d >= 0 and d < 9 :
        print('서울 입니다')
    else :
        print('서울이 아닙니다')
print("---------------------------------")
print()

# 129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
print('129')
id = input('주민등록번호: ')
day,iden = id.split('-')
sum = 0
for i in range(0,8) :
    if i < 6 :
        sum += int(day[i])*(i+2)
    else :
        sum += int(iden[i-6])*(i+2)
for i in range(2,6):
    r = int(iden[i])*i
    sum += r
if (11 - sum%11 == int(iden[-1])) :
    print('유효한 주민등록번호입니다.')
else :
    print('유효하지 않은 주민등록번호입니다.')
print("---------------------------------")
print()

# 130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장"
# 그렇지 않은 경우 "하락장" 문자열을 출력하라.
# Key Name                  Description
# opening_price           최근 24시간 내 시작 거래금액
# closing_price           최근 24시간 내 마지막 거래금액
# min_price               최근 24시간 내 최저 거래금액
# max_price               최근 24시간 내 최고 거래금액
print('130')
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

d = eval(btc['max_price']) - eval(btc['min_price'])
x = eval(btc['opening_price']) + d
y = eval(btc['max_price'])
if x > y:
    print('상승장')
else :
    print('하락장')
print("---------------------------------")
print()

