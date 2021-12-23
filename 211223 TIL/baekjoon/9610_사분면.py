n = int(input('점의 개수 : '))
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
for _ in range(n):
    # (-106 ≤ xi, yi ≤ 106)
    X, Y = map(int, input('점의 좌표 : ').split(' '))
    if X > 0 and Y > 0:
        Q1 += 1

    elif X < 0 and Y > 0:
        Q3 += 1

    elif X < 0 and Y < 0:
        Q3 += 1

    elif X > 0 and Y < 0:
        Q4 += 1

    else:
        AXIS += 1


print(f'Q1 : {Q1}\nQ2 : {Q2}\nQ3 : {Q3}\nQ4 : {Q4}\nAXIS : {AXIS}')