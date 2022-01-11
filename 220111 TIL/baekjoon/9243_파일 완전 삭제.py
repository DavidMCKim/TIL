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
#
# N = int(input())
# a, b = list(input()), list(input())
# for _ in range(N):
#     for i in range(len(a)):
#         if a[i] == '0':
#             a[i] = '1'
#         else:
#             a[i] = '0'
# print("Deletion succeeded" if a == b else "Deletion failed")