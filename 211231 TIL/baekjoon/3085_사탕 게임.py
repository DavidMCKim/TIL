def x():
    global max_count, temp, N
    for x in range(N):
        count = 1
        for y in range(1,N):
            if candy_color[x][y] == candy_color[x][y-1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 1

        if max_count < count:
            max_count = count


def y():
    global max_count, temp, N
    for x in range(N):
        count = 1
        for y in range(N):
            print(y)
    pass

N = int(input())
candy_color = [input() for x in range(N)]
max_count = 0
temp = ''


max_width = x()
print(max_width)
