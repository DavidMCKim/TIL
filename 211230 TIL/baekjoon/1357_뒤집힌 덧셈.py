def Rev(num):
    num = str(num)
    new_num = ''
    for _ in range(len(num)-1,-1,-1):
        new_num += num[_]
    new_num = int(new_num)
    return new_num

X, Y = map(int,input().split(' '))
result = Rev(Rev(X)+Rev(Y))
print(result)