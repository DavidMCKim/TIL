# 02984 -> 576
# 567 -> 210
N = list(map(int,input()))
print(N)
result = N[0]
for i in range(1,len(N)):
    if i <= 1 or result <= 1:
        result += N[i]
    else:
        result *= N[i]
print(result)