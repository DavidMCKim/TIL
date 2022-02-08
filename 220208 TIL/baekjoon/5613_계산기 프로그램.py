#########################################################################################################################################
##ver.단순구현
## 틀린이유 : 나눗셈결과값에서 소수점이하를 버리지 않아서..
sum_num = 0
num = []
while True:
    n = input()
    num.append(n)
    if n == '=':
        for i, a in enumerate(num):
            if a == '=':
                print(sum_num)
                break
            if i == 1:
                if a == '+':
                    sum_num = int(num[i - 1]) + int(num[i + 1])
                if a == '*':
                    sum_num = int(num[i - 1]) * int(num[i + 1])
                if a == '-':
                    sum_num = int(num[i - 1]) - int(num[i + 1])
                if a == '/':
                    sum_num = int(int(num[i - 1]) / int(num[i + 1]))
            else:
                if a == '+':
                    sum_num += int(num[i + 1])
                if a == '*':
                    sum_num *= int(num[i + 1])
                if a == '-':
                    sum_num -= int(num[i + 1])
                if a == '/':
                    sum_num = int(sum_num / int(num[i + 1]))
        break