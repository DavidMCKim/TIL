point_x = []
point_y = []

for _ in range(3):
    x,y = map(int,input().split(' '))
    point_x.append(x)
    point_y.append(y)

for _ in range(3):
    print(point_x.count(point_x[_]))
    print(point_y.count(point_y[_]))
    if point_x.count(point_x[_]) == 1:
        X = point_x[_]
    if point_y.count(point_y[_]) == 1:
        Y = point_y[_]

print(f'네번째점 : {X}, {Y}')