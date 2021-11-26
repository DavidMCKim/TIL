def sabunmeon(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y < 0:
        print(3)
    else:
        return "잘못된 입력입니다."


x = int(input())
y = int(input())

sabunmeon(x, y)
