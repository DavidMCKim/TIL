# 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1,1)이며, 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸 씩 이동할 수 있습니다.
# 이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출 할 수 있는 형태로 제시됩니다.
# 이 때 동빈이가 탈출하기 위해 움직여야 하는 최소칸의 개수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.


## 1:52 ~

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx >=N or ny<0 or ny >=M:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y]+1
                queue.append((nx,ny))
    return miro[N-1][M-1]

N,M = map(int,input().split())
miro = []

for i in range(N):
    miro.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

