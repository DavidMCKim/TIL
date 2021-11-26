# 정수 3개를 입력 받아서 제일 큰 수 출력

########################################
# 강사님 코드

## 1. 정수 3개 입력받아 변수에 저장
num1 = int(input('정수 1 입력 : '))
num2 = int(input('정수 2 입력 : '))
num3 = int(input('정수 3 입력 : '))

## 2. 저장된 3개의 변수 중 제일 큰 수 판별
# num1이 가장 큰 경우 : num1 > num2 and num1 > num3
if((num1 > num2) and (num2 > num3)) :
    print('재일 큰 수 : ', num1) ## 3. 판별된 제일 큰수 출력

# num1이 가장 큰 수가 아니면 : num >2 num3 => num2가 가장 큰수
elif num2 > num3 :
    print('제일 큰 수 : ', num2) ## 3. 판별된 제일 큰수 출력

# num2도 제일 큰 수가 아니면 : num3이 가장 큰 수
else :
    print('제일 큰 수 : ', num3) ## 3. 판별된 제일 큰수 출력




########################################
# 내 코드
a = int(input("정수1 입력 : "))
b = int(input("정수2 입력 : "))
c = int(input("정수3 입력 : "))


if (a >= b) :
    if (a > c) :
         print("제일 큰 수 : %d" % a)
    else :
         print("제일 큰 수 : %d" % c)
else :
    if (b >= c):
         print("제일 큰 수 : %d" % b)
    else :
         print("제일 큰 수 : %d" % c)