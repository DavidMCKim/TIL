def solution(people, limit):
    answer = 0
    people.sort()
    index = 0
    max_value = len(people)-1
    while max_value >= index:
        answer += 1
        if people[max_value]+people[index] <= limit:
            index += 1
        max_value -= 1
    return answer