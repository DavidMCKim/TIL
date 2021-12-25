def del_zero(lottos,zero):
    for _ in range(zero):
        lottos.pop(0)

def count_same(lottos,win_nums):
    i = 0
    for _ in range(len(lottos)):
        if lottos[_] in win_nums:
            i += 1

def solution(lottos, win_nums):
    i = 0
    answer = []
    lottos.sort()
    win_nums.sort()
    zero = lottos.count(0) # lottos 배열 안에 0의 개수
    if zero == 6:
        answer.append(1)
        answer.append(6)

    elif zero == 5:
        del_zero(lottos,zero)
        if lottos[0] in win_nums:
            answer.append(1)
            answer.append(6)
        else:
            answer.append(2)
            answer.append(6)

    elif zero == 4:
        for _ in range(len(lottos)):
            if lottos[_] in win_nums:
                i +=1
        if i == 2:
            answer.append(1)
            answer.append(5)
        elif i == 1:
            answer.append(2)
            answer.append(6)

    elif zero == 3:
        for _ in range(len(lottos)):
            if lottos[_] in win_nums:
                i += 1
        if i == 3:
            answer.append(1)
            answer.append(4)
        elif i == 2:
            answer.append(2)
            answer.append(5)
        elif i == 1:
            answer.append(3)
            answer.append(6)

    elif zero == 2:
        for _ in range(len(lottos)):
            if lottos[_] in win_nums:
                i += 1
        if i == 4:
            answer.append(1)
            answer.append(3)
        elif i == 3:
            answer.append(2)
            answer.append(4)
        elif i == 2:
            answer.append(3)
            answer.append(5)
        elif i == 1:
            answer.append(4)
            answer.append(6)

    elif zero == 1:
        for _ in range(len(lottos)):
            if lottos[_] in win_nums:
                i += 1
        if i == 5:
            answer.append(1)
            answer.append(2)
        elif i == 4:
            answer.append(2)
            answer.append(3)
        elif i == 3:
            answer.append(3)
            answer.append(4)
        elif i == 2:
            answer.append(4)
            answer.append(5)
        elif i == 1:
            answer.append(5)
            answer.append(6)

    else:
        for _ in range(len(lottos)):
            if lottos[_] == win_nums[_]:
                i += 1
        if i == 6:
            answer.append(1)
            answer.append(1)
        elif i == 5:
            answer.append(2)
            answer.append(2)
        elif i == 4:
            answer.append(3)
            answer.append(3)
        elif i == 3:
            answer.append(4)
            answer.append(4)
        elif i == 2:
            answer.append(5)
            answer.append(5)
        else:
            answer.append(6)
            answer.append(6)
    print(answer)
    return answer

## 예외처리 필요
## https://www.acmicpc.net/board/view/38435 사이트 참고
try:
    num1 = input().split(' ')
    lottos = [int(_) for _ in num1]
    num2 = input().split(' ')
    win_nums = [int(_) for _ in num2]
    solution(lottos, win_nums)
except:
    exit

