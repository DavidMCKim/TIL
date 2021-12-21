T = int(input('테스트의 개수 : '))

for _ in range(T):
    A = input('숫자(정수 or 소수 첫째자리)와 화성 연산자(최대3개)를 입력해주세요.:').split(' ')
    s = float(A[0])
    for i in range(len(A)):
        if A[i] == '@':
            s *= 3
        elif A[i] == '#':
            s -= 7
        elif A[i] == '%':
            s += 5

    print('%0.2f' % s)