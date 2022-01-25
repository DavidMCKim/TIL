N,M = map(int,input().split())
fishbread = [input() for i in range(N)]

for x in range(N):
    for y in range(M-1,-1,-1):
        print(fishbread[x][y],end='')
    print()