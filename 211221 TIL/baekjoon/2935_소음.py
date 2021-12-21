A = int(input())
cal = input()
B =  int(input())
if A%10 == 0 and B%10 == 0:
    if cal == '+':
        print(A+B)
    elif cal == '*':
        print(A*B)
    else:
        print('잘못된 연산자 입력입니다.')
else:
    print('입력된 수의 형태가 잘못되었습니다.')