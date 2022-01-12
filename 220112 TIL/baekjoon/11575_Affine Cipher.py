def alpha_to_num(X):
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_dict = {}
    for alpha, index in enumerate(alpha_list):
        alpha_dict[index] = alpha

    return int(alpha_dict[X])

def E(a,b,X):
    return (a*alpha_to_num(X) + b)%26

def num_to_alpha(X):
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    num_dict = {}
    for alpha, index in enumerate(alpha_list):
        num_dict[alpha] = index
    return num_dict[X]

T = int(input())
for i in range(T):
    a,b = map(int,input().split(' '))
    s = input()
    for _ in s:
        print((a*ord(_)+b)%26,end=' ')
        # print(num_to_alpha(E(a,b,_)),end='')

