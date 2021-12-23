test = int(input())


for _ in range(test):
    OX = input()
    score = 0
    i = 0
    for num in range(len(OX)):
        if num == 0:
            if OX[num] == 'O':
                i += 1
                score += 1
            else:
                i = 0
        else:
            if OX[num] == 'X':
                i = 0
            else:
                if OX[num-1] == 'X':
                    i = 1
                    score += 1
                else:
                    i += 1
                    score += i

    print(score)
