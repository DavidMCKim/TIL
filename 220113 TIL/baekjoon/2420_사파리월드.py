#### 오답
# N, M = map(int,input().split(' '))
# if N < 0 :
#     print(M-N)
# elif M < 0:
#     print(N-M)
# else:
#     print(abs(N-M))

#### 정답
N, M = map(int,input().split(' '))
print(abs(N-M))