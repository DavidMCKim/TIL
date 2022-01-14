N = int(input())
num_list = list(map(int,input().split(' ')))
for _ in sorted(set(num_list)):
    print(_,end=' ')