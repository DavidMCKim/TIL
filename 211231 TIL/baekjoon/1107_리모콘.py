N = int(input())
click = abs(100 - N)
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for n in str(num):
        if n in broken:
            break
    else:
        click = min(click, len(str(num)) + abs(num - N))
print(click)