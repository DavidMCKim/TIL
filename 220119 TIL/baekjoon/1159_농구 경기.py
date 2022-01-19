## 사전순으로 출력하기를 빼먹음..

N = int(input())

name_list = [input() for _ in range(N)]

first_name_list = [name[0] for name in name_list]
first_name_list.sort()
first_name_set = list(set(first_name_list))
first_name_set.sort()

player = ''
for alpha in first_name_set:
    if first_name_list.count(alpha) >= 5:
        player += alpha

if len(player) != 0:
    print(player)
else:
    print('PREDAJA')