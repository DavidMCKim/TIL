N,M = map(int,input().split())
friend = [0 for i in range(N)]
for i in range(M):
    A, B = map(int,input().split())
    friend[A-1] += 1
    friend[B-1] += 1
for num in friend:
    print(num)