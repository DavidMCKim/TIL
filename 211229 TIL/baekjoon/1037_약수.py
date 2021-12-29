# 1번째 오답 : 런타임에러
N = int(input())
real = []
for _ in range(N):
    num = int(input())
    real.append(num)
real.sort()
print(real[0]*real[-1])

# 2번째 오답 : 런타임에러
N = int(input())
real = []
for _ in range(N):
    num = int(input())
    real.append(num)
print(max(real)*min(real))

# 정답..
N = int(input())
real = list(map(int,input().split(' ')))
print(max(real)*min(real))