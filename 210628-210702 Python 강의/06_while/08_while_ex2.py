# 08_while_ex2.py

# 1부터 사용자가 입력한 숫자까지의 홀수의 합을 구하는 프로그램을 while 문으로 작성하시오
# 마지막 숫자를 입력하세요 : 10
# 1부터 10까지의 홀수의 합은 25입니다.

###########################################
# 내 코드
last = int(input('마지막 숫자를 입력하세요: '))
sum = 0
i = 0
while i <= (last-1):
    i += 1
    if i%2 != 0:
        sum += i
        # print(i)
        # print('sum:',sum)
print('1부터 %d까지의 홀수의 합은 %d 입니다.' %(last,sum) )

###########################################
# 강사님 코드

su = int(input('마지막 숫자를 입력하세요 : '))

i = 0 # 초기 변수
sum = 0 # 누적 변수

while i <= su :
    if i%2 == 1: # 홀수인지 확인
        sum += i

    i += 1

print('1부터',su,'까지 홀수의 합은',sum,'입니다')