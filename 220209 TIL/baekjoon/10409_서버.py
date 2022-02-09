n,T = map(int,input().split())
time_list = list(map(int,input().split()))
for i in range(n):
    if sum(time_list[:i+1]) > T:
        print(i)
        break
    elif i == n-1:
        print(n)