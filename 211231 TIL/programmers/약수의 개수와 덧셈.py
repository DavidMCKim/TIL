def solution(left, right):
    answer = 0
    for _ in range(left, right + 1):
        yaksu = 0
        for num in range(1, _ + 1):
            if _ % num == 0:
                yaksu += 1

        if yaksu % 2 == 0:
            answer += _
        else:
            answer -= _

    return answer