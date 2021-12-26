N = int(input())
OX = input().split(' ')
for _ in range(len(OX)):
    OX[_] = int(OX[_])

score = 0
i = 0
for num in range(len(OX)):
    if num == 0:
        if OX[num] == 1:
            i += 1
            score += 1
        else:
            i = 0
    else:
        if OX[num] == 0:
            i = 0
        else:
            if OX[num-1] == 0:
                i = 1
                score += 1
            else:
                i += 1
                score += i

print(score)
