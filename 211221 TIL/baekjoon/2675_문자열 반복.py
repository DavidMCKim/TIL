T = int(input('테스트의 개수 : '))

for _ in range(T):
    S, R = input(f'{int(_)+1}. 반복횟수(S)와 문자열(R)을 입력하시오 : ').split(' ')
    P = ''
    for item in R:
        P += int(S)*item
    print(P)
