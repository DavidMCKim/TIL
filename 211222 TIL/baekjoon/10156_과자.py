K,N,M = map(int,input().split(' '))
change = (K * N) - M
if change >= 0:
    print(change)
else:
    print(0)