## 시간초과
# N, K = map(int,input().split())
# value = [input() for i in range(N)]
# value = value[::-1]
# count = 0
# for i in value:
#     i = int(i)
#     if K >= i:
#         while K >= i:
#             if K < i:
#                 break
#             else:
#                 K -= i
#                 count += 1
# print(count)


N, K = map(int,input().split())
value = [input() for i in range(N)]
value = value[::-1]
count = 0
for i in value:
    i = int(i)
    if K >= i:
        count += K//i
        K -= i*(K//i)
        if K == 0:
            break
print(count)