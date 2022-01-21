## list를 이용한 풀이 - 내꺼
T = int(input())
for _ in range(T):
    text = input()
    reverse_text = text.split(' ')
    for i in range(len(reverse_text)):
        for alpha in range(len(reverse_text[i])-1,-1,-1):
            print(reverse_text[i][alpha],end='')
        print(' ',end='')
    print()

## list를 이용한 풀이 - 인터넷
# N = int(input())
# for i in range(N):
#     string = list(input().split())
#     for j in string:
#         print(j[::-1], end=' ')

## stack을 이용한 풀이 - 인터넷
# N = int(input())
# for i in range(N):
#     string = input()
#     string += ' '
#     stack = []
#     for j in string:
#         if j != ' ':
#             stack.append(j)
#         else:
#             while stack:
#                 print(stack)
#                 print(stack.pop(), end='')
#             print(' ',end='')