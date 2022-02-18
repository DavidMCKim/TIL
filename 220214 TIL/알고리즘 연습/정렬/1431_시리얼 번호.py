## 두 코드 모두 시간 메모리 동일!!

# def sum_digit(data):
#     num = 0
#     for i in data:
#         if i.isdigit():
#             num += int(i)
#     return num
#
# N = int(input())
# sirial_num = [input() for i in range(N)]
# sirial_num.sort(key=lambda x:(len(x),sum_digit(x),x))
# print(*sirial_num,sep='\n')

# def sum_digit(data):
#     num = 0
#     for i in data:
#         if i.isdigit():
#             num += int(i)
#     return num
#
# N = int(input())
# sirial_num = [input() for i in range(N)]
# sirial_num.sort(key=lambda x:(len(x),sum_digit(x),x))
# for i in sirial_num:
#     print(i)