def solution(numbers):
    answer = []
    for x in range(len(numbers)):
        for y in range(1,len(numbers)):
            if x != y:
                if numbers[x] + numbers[y] not in answer:
                    answer.append(numbers[x] + numbers[y])
    answer.sort()
    return answer

numbers = [5,0,2,7]
answer = solution(numbers)
print(answer)