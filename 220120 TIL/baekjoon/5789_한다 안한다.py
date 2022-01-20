T = int(input())
count = 0
for _ in range(T):
    test = input()
    half = int(len(str(test))/2)
    if test[half-1] == test[half]:
        print('Do-it')
    elif test[half-1] != test[half]:
        print('Do-it-Not')
