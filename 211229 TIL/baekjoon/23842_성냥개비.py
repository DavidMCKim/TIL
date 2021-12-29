# 15시30분 시작 -

# 수식 형태 : xx + xx = xx, 0~9
# 모든 수는 항상 두자리수 -> ex) 27 -> 27, 5 -> 05
# '+', '=' 도 성냥개비 2개
# N개의 성냥개비를 모두 상요하여 만족하는 수식? 없다면 impossible 출력

# 풀이
# +와 =는 반드시 포함되기때문에 세 수의 합이 N-4 가 되면서 앞의 두수의 합이 마지막 수가 되어야 함

# 1 - 2
# 2 - 5
# 3 - 5
# 4 - 4
# 5 - 5
# 6 - 6
# 7 - 3
# 8 - 7
# 9 - 6
# 0 - 6


# 10*x+y + 10*x+y = 10*x+y

N = int(input())
int_dict = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6,0:6}
keys_list = []
possible_list = []
for x in range(len(int_dict.keys())):
    for y in range(1,len(int_dict.keys())):
        for z in range(2,len(int_dict.keys())):
            if x + y == z:
                keys_list.append([x,y,z])
for _ in keys_list:
    if int_dict[_[0]] + int_dict[_[1]] + int_dict[_[2]] == N-4:
        possible_list.append(_)

if possible_list != []:
    for _ in possible_list:
        pass


 # = N - 4