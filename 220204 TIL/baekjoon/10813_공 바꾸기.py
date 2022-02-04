N,M = map(int,input().split())
bascket = [i+1 for i in range(N)]
for num in range(M):
    i, j = map(int, input().split())
    temp = bascket[i-1]
    bascket[i-1] = bascket[j-1]
    bascket[j-1] = temp
for i in bascket:
    print(i, end=' ')