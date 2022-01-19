# def solution(n, lost, reserve):
#     answer = n - len(lost)

#     for i in lost:
#         if i - 1 in reserve:
#             answer += 1
#             reserve.remove(i - 1)
#         elif i + 1 in reserve:
#             answer += 1
#             reserve.remove(i + 1)
#
#     return answer


####
# 1. 여분이 있는친구가 잃어버렸을 경우 생각 안해서
# 2. 왜 reserve에서 빼면 안되는지 노 이해..!!

def solution(n, lost, reserve):
    reserve_but_lost = set(reserve) - set(lost)
    lost_not_reserve = set(lost) - set(reserve)

    for i in reserve_but_lost:
        if i - 1 in lost_not_reserve:
            lost_not_reserve.remove(i - 1)
        elif i + 1 in lost_not_reserve:
            lost_not_reserve.remove(i + 1)
    answer = n - len(lost_not_reserve)
    return answer