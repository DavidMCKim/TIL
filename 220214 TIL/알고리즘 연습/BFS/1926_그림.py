# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

n,m = map(int,input().split())
picture = []
for y in range(n):
    picture.append(list(map(int,input().split())))

cnt = 0 # 그림의 개수
queue = [] # 1의 위치
current = [0,0] # 현재위치

for x in picture:
    for y in x:
        