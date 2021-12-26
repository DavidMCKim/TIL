N = int(input())
list = []
for _ in range(N):
    n, d, m, y = input().split(' ')
    list.append([int(y), int(d), int(m), n])
    list.sort()

print(max(list)[-1])
print(min(list)[-1])