passenger = 0
train = []
for _ in range(4):
    IN, OUT = map(int,input().split(' '))
    passenger += OUT
    passenger -= IN
    train.append(passenger)

print(max(train))