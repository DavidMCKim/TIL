# 대략 2시간 정도 걸림..
N,M = map(int,input().split(' '))
for x in range(N):
    stack_L = []
    stack_R = []
    color = input()
    color_list = [' ' for _ in range(len(color))]
    a = 0
    b = -1
    for _ in range(len(color)):
        if _ <= (len(color)-1)/2:
            stack_L.append(color[_])
        else:
            stack_R.append(color[_])
    for _ in range(len(stack_R)):
        if stack_L[a] == stack_R[b]:
            color_list[a] = color_list[b] = stack_L[a]
        else:
            if stack_R[b] != stack_L[a] == '.':
                color_list[a] = color_list[b] = stack_R[b]
            elif stack_L[a] != stack_R[b] == '.':
                color_list[a] = color_list[b] = stack_L[a]
            elif stack_L[a] == stack_R[b] == '.':
                color_list[a] = color_list[b] = '.'
        a += 1
        b -= 1
    print(''.join(color_list))