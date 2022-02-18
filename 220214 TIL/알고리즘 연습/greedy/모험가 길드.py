N = int(input())
traveler = list(map(int,input().split()))
traveler.sort()
result, count = 0,0
for i in traveler:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)