date = int(input())
illegal = 0
car_num = map(int,input().split(' '))
for _ in car_num:
    if _ == date:
        illegal += 1
print(illegal)