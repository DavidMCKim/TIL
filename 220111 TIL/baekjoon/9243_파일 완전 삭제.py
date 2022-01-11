n = int(input())
normal = list(input())
result = list(input())

for num in range(n):
    for _ in range(len(normal)):
        if normal[_] == '1':
            normal[_] = '0'

        elif normal[_] == '0':
            normal[_] = '1'

if normal == result:
    print('Deletion succeeded')
else:
    print('Deletion failed')