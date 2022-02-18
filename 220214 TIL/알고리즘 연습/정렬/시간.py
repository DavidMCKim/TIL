# 00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 출력
# 입력 : 5 / 출력 11475
N = int(input())
cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
print(cnt)