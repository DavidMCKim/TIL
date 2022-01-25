# apple = list(map(int,input().split()))
# orange = list(map(int,input().split()))
# count = 0
# for i in range(apple[1]):
#     while apple[1] != 0:
#         apple[1] -= 1
#         orange[1] += 1
#         count += 1
# for i in range(orange[0]):
#     while orange[0] != 0:
#         orange[0] -= 1
#         apple[0] += 1
#         count += 1
# print(count)

A,B = list(map(int,input().split()))
C,D = list(map(int,input().split()))

print(min(A+D,B+C))