def reverse(i,j,bascket):
    if i == 1:
        for num in bascket[j - 1::-1]:
            bascket[i - 1] = num
            i += 1
    for num in bascket[j-1:i-2:-1]:
        bascket[i-1] = num
        i += 1

N,M = map(int,input().split())
bascket = [i+1 for i in range(N)]
for i in range(M):
    i,j = map(int,input().split())
    reverse(i, j, bascket)
print(*bascket)