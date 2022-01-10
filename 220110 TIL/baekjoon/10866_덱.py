# def empty():
#     global Deque
#     if len(Deque) == 0:
#         return 1
#     else:
#         return 0
#
# def push_front(X):
#     global Deque
#
#     length = len(Deque)
#     Deque.append('None')
#
#     for _ in range(length,-1,-1):
#         temp = Deque[_]
#         Deque[_+1] = temp
#         Deque[_] = 'None'
#
#     return
#
#
# def push_back(X):
#     global Deque
#     Deque.append(X)
#     return
#
# def pop_front():
#     global Deque
#     if empty():
#         return 0
#     else:
#         front = Deque[0].pop
#         return front
#
# def pop_back():
#     global Deque
#     if empty():
#         return 0
#     else:
#         back = Deque[-1].pop
#         return back
#
# def size():
#     size = len(Deque)
#     return size

# def empty():

Deque = []
N = int(input())
for i in range(N):
    command = input()
    if 'push_back' in command:
        Deque.append(command.split(' ')[1])

    elif 'push_front' in command:
        Deque.insert(0,command.split(' ')[1])

    elif command == 'pop_front':
        if len(Deque) == 0:
            data = -1
        else:
            data = Deque.pop(0)
        print(data)

    elif command == 'pop_back':
        if len(Deque) == 0:
            data = -1
        else:
            data = Deque.pop(-1)
        print(data)

    elif command == 'size':
        print(len(Deque))

    elif command == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if len(Deque) == 0:
            data = -1
        else:
            data = Deque[0]
        print(data)

    elif command == 'back':
        if len(Deque) == 0:
            data = -1
        else:
            data = Deque[-1]
        print(data)
