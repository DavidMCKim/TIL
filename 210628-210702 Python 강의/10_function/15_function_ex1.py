# 15_function_ex1.py

# 다음의 함수를 포함하는 프로그램 작성
# 함수 이름 : sum()
# 숫자 2개를 입력 받아서 두수의 합을 구하여 출력

# 숫자1 입력 : 3
# 숫자2 입력 : 4
# 합 : 7

def sum() :
    num1 = int(input('숫자1 입력 : '))
    num2 = int(input('숫자2 입력 : '))
    sum = num1+ num2
    return sum

print('합 : ', sum())