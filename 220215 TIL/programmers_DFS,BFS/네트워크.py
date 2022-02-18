def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if computers[x][y] == 1:
        computers[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(n):
        if dfs(x, y) == True:
            answer += 1
print(answer)