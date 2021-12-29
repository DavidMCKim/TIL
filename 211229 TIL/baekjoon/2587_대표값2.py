# num_list = []
# for _ in range(5):
#     N = int(input())
#     num_list.append(N)
# print(int(sum(num_list)/len(num_list)))
# num_list.sort()
# print(num_list[2])
#
# # 틀린이유 : 3번째 위치의 index는 2이다..3이 아니고..후..정신차리자..!!

h,m = map(int,input().split(' '))

if h >= 1 and m < 45:
    print(h-1, end=' ')
    print(m+60-45)
elif h == 0 and m < 45:
    print(23, end=' ')
    print(m+60-45)
else:
    print(h, end=' ')
    print(m-45)