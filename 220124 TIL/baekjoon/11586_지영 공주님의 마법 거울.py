N = int(input())
mirror = []
for i in range(N):
    mirror.append(input())
K = int(input())


def original():
    for i in range(N):
        for j in range(N):
            print(mirror[i][j],end='')
        print('')


def reverse_row():
    for i in range(N):
        for j in range(N - 1, -1, -1):
            print(mirror[i][j],end='')
        print('')


def reverse_column():
    for i in range(N - 1, -1, -1):
        for j in range(N):
            print(mirror[i][j],end='')
        print('')
if K == 1:
    original()
elif K == 2:
    reverse_row()
elif K == 3:
    reverse_column()
# mirror_reverse = []
# if K == 1:
#     for x in mirror:
#         for i,num in enumerate(x):
#             if i%7==0 and i!=0:
#                 print(num)
#             else:
#                 print(num,end='')
# elif K == 2:
#     for x in mirror:
#         temp = []
#         for i in range(len(x)-1,-1,-1):
#             temp.append(x[i])
#         print(''.join(temp))
#
# elif K == 3:
#     a = 0
#     b = -1
#     for x in range(len(mirror)-1,-1,-1):
#         print(mirror[x])