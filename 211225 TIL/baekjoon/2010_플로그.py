N = int(input())
total = 0
for _ in range(N):
    multitap = int(input())
    total += multitap
print(total-(N-1))