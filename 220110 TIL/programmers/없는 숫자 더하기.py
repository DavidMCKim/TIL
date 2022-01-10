def solution(numbers):
    answer = -1
    none_list = []
    num_list = [num for num in range(10)]
    for num in num_list:
        if num not in numbers:
            none_list.append(num)
        else:
            pass
    print(none_list)
    answer = sum(none_list)
    return answer

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))

