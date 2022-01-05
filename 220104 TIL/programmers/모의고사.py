def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    count1,count2,count3 = 0, 0, 0

    for _ in range(len(answers)):
        index1 = _%5
        index2 = _%8
        index3 = _%10

        if num1[index1] == answers[_]:
            count1 += 1
        if num2[index2] == answers[_]:
            count2 += 1
        if num3[index3] == answers[_]:
            count3 += 1

    max_count = max(count1,count2,count3)
    answer = []

    if max_count == count1:
        answer.append(1)
    if max_count == count2:
        answer.append(2)
    if max_count == count3:
        answer.append(3)

    return answer