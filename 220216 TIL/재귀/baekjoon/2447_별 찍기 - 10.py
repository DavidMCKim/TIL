def star(num):
    for x in range(num):
        for y in range(num):
            if x >= num/3 and x<=num-(num/3)-1 and y >= num/3 and y<=num-(num/3)-1:
                print(' ',end='')
            else:
                print('*',end='')
        if x != num-1:
            print()

N = int(input())
star(N)