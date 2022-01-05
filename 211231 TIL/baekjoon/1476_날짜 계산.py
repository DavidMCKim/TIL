E,S,M = map(int,input().split(' '))
count = 1
x = y = z = 1
while True:
    if x == E and y == S and z == M:
        break

    x += 1
    y += 1
    z += 1
    count += 1

    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1

print(count)