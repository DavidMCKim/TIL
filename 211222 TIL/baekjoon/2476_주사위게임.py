N = int(input('참여하는 사람 수 : '))

num = []

for _ in range(N):
    A,B,C = map(int,input('나온 주사위의 수 : ').split(' '))

    if A == B and B == C:
        a = 10000+(A*1000)
    elif (A == B and B != C) or (B == C and A != B):
        a = 1000 + B * 100
    elif A == C and B != C:
        a = 1000 + A * 100
    else:
        a = max(A,B,C) * 100

    num.append(a)


print('가장 많은 상금 : ',max(num))