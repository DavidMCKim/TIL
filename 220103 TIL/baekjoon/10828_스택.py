# N = int(input())
# stack = []
# top = -1
# for _ in range(N):
#     command = input()
#     if 'push' in command:
#         num = int(command.lstrip('push '))
#         stack.append(num)
#
#     if command == 'pop':
#         length = len(stack)
#         if length == 0:
#             print(-1)
#         else:
#             print(stack[length-1])
#             stack = stack[:length-1]
#             print(stack)
#
#     if command == 'size':
#         print(len(stack))
#
#     if command == 'empty':
#         if len(stack) != 0:
#             print(0)
#         else:
#             print(1)
#
#     if command == 'top':
#         length = len(stack)
#         if length == 0:
#             print(-1)
#         else:
#             print(stack[length - 1])


###################################################################

N = int(input())
stack = []
for _ in range(N):
    command = input().split(' ')
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

###################################################################
# import sys
# n = int(sys.stdin.readline())
#
# stack=[]
# for i in range(n):
#     command = sys.stdin.readline().split()
#
#     if command[0]=='push':
#         stack.append(command[1])
#     elif command[0]=='pop':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack)==0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'top':
#         if len(stack)==0:
#             print(-1)
#         else:
#             print(stack[-1])