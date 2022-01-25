def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    while bridge != []:
        answer += 1
        bridge.pop(0)
        if truck_weights != []:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
answer = 0
bridge = [0 for i in range(bridge_length)]
while bridge != []:
    answer += 1
    bridge.pop(0)
    if truck_weights != []:
        if sum(bridge)+truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
print(answer)

# trucks_on_bridge = [0] * bridge_length
# while len(trucks_on_bridge):
#     answer += 1
#     trucks_on_bridge.pop(0)
#     print(trucks_on_bridge)
#     if truck_weights:
#         if sum(trucks_on_bridge) + truck_weights[0] <= weight:
#             trucks_on_bridge.append(truck_weights.pop(0))
#             print(trucks_on_bridge)
#         else:
#             trucks_on_bridge.append(0)
# print(trucks_on_bridge)
# print(answer)