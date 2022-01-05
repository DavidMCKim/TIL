def solution(participant, completion):
    answer = ''
    for _ in participant:
        if _ not in completion:
            completion.pop(_)
            answer += _
    return answer

answer = ''
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = {}
for i in participant:
    answer[i] = answer.get(i, 0) +1
for j in completion:
    answer[j] -= 1
for k in answer:
    if answer[k] :
        print(k)

# for _ in range(len(participant)):
#     if participant[_] in completion:
#         print(_)
#     if participant[_] not in completion:
#         answer += participant[_]
# print(answer)
#
# participant.pop(0)
# print(participant)
#
#
# def solution(participant, completion):
#     answer = {}
#     for i in participant:
#         answer[i] = answer.get(i, 0) +1
#     for j in completion:
#         answer[j] -= 1
#     for k in answer:
#         if answer[k] :
#             return k