# K = 아이들이 한 종류의 사탕을 최소한 먹어야 하는 개수
# N = 사탕의 종류
answer = 0
T = int(input())
for i in range(T):
    N,K = map(int,input().split(' '))
    candy = list(map(int,input().split(' ')))
    for num in candy:
        answer += divmod(num,K)[0]
    print(answer)
    answer = 0