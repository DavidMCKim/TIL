# NxM 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분까지 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음의 4x5 얼음 틀 예시에서는 총 3개 생성됩니다
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

def dfs(x,y):
    if x<=-1 or x >= N  or y<= -1 or y >= M:
        return False
    if ice[x][y] == 0:
        ice[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
N,M = map(int,input().split())
answer = 0
ice = []
for i in range(N):
    ice.append(list(map(int,input().split())))

for x in range(N):
    for y in range(M):
        if dfs(x,y) == True:
            answer += 1
print(answer)