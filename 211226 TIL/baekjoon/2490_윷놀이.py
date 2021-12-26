for _ in range(3):
    A = input().split(' ')
    zero = A.count('0')
    if zero == 0:
        print('E')
    elif zero == 1:
        print('A')
    elif zero == 2:
        print('B')
    elif zero == 3:
        print('C')
    elif zero == 4:
        print('D')
