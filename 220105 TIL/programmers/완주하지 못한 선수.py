def solution(participant, completion):
    answer = ''
    player = {}
    for i in participant:
        if i in player.keys():
            player[i] += 1
        else:
            player[i] = 1

    for i in completion:
        if i in player.keys():
            player[i] -= 1

    for i in player.keys():
        if player[i] != 0:
            answer += i
    return answer

answer = {}
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = ''
player = {}
for i in participant:
    if i in player.keys():
        player[i] += 1
    else:
        player[i] = 1

for i in completion:
    if i in player.keys():
        player[i] -= 1

for i in player.keys():
    if player[i] != 0:
        answer += i
print(answer)