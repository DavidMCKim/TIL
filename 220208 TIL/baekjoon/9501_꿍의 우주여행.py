T = int(input())
for x in range(T):
    count = 0
    N,D = map(int,input().split())
    for y in range(N):
        V,F,C = map(int,input().split())
        if (F/C)*V >= D:
            count += 1
    print(count)