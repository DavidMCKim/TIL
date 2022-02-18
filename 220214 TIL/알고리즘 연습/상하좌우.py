N = int(input())
plan = list(input().split())
x,y = 1,1
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move = ['U','D','L','R']

for p in plan:
    for i in range(len(move)):
        if p == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x,y = nx,ny
print(x,y)