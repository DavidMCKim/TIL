# 05_for_ex2.py

# 정수 2개를 입력 받아서 두 수 사이의 합을 구하는 프로그램 작성 (for 문 사용)
#################################
# 강사님 코드
# 정수 2개 입력 받기
print('숫자 1이 더 작은 정수를 입력하세요')
num1 = int(input("숫자1 입력 : "))
num2 = int(input("숫자2 입력 : "))

sumx = 0

for x in range(num1, num2+1):
    sumx += x
print('%d부터 %d까지의 합 : %d'%(num1, num2, sumx))


#################################
# 내 코드

# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
# sum = 0
#
# if num1>num2 :
#     for i in range(num2, num1 + 1):
#         sum += i
#     print('%s부터 %s까지의 합 : %s' % (num2, num1, sum))
# else :
#     for i in range(num1, num2 + 1):
#         sum += i
#     print('%s부터 %s까지의 합 : %s' % (num1, num2, sum))




