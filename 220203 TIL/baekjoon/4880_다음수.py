## 등차수열 : 인접한 두 수의 차이(공차)가 일정한 수열
def AP(num):
    gongcha = num[1] - num[0]
    num.append(num[-1]+gongcha)
    return num[-1]

## 등비수열 : 각 항이 그 앞과 일정한 비(공비)를 가지는 수열
def GP(num):
    gongb = num[1] / num[0]
    num.append(int(num[-1] * gongb))
    return num[-1]

num = [-1,-1,-1]
if __name__ == '__main__':
    while True:
        num = list(map(int,input().split()))
        if num == [0, 0, 0]:
            break
        elif num[2]-num[1] == num[1]-num[0]:
            print('AP', AP(num))
        elif num[2]/num[1] == num[1]/num[0]:
            print('GP', GP(num))