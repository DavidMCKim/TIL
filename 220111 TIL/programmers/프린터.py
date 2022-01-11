def solution(priorities, location):
    answer = 0
    Queue = [(i,p) for i,p in enumerate(priorities)]

    while True:
        J = Queue.pop(0)
        if any(J[1] < queue[1] for queue in Queue):
            Queue.append(J)
        else:
            answer += 1
            if J[0] == location:
                return answer








    return answer

priorities = [2, 1, 3, 2]
location = 2
solution(priorities, location)
#
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0

#######################################

# priorities = [2, 1, 3, 2]
# location = 2
#
# temp = priorities
# temp.sort(reverse=True)
# print(temp.index(location))