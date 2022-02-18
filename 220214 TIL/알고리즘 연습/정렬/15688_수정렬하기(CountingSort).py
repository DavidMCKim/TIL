# Counting Sort는 수의 범위가 1000만 이하일 때 사용
# N = int(input())
# num = [int(input()) for i in range(N)]
# num.sort()
# print(*num,sep='\n')

N = int(input())
num = [int(input()) for i in range(N)]
num.sort()
for i in num:
    print(i)