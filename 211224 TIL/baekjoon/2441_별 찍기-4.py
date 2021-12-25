N = int(input())
i = N
for _ in range(N,0,-1):
    print(' '*(N-i)+'*'*_)
    i -= 1