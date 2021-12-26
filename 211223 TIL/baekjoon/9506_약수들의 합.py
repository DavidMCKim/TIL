n = 0
while n != -1:
    n = int(input())
    yaksu = []
    result = ''
    for _ in range(1,n):
        if n % _ == 0:
            yaksu.append(_)

        else:
            pass
    print(yaksu)
    if n == sum(yaksu):
        for _ in yaksu:
            if _ == 1:
                result += str(_)
            else:
                result += ' + ' + str(_)
        print(f'{n} = {result}')
    else:
        print(f'{n} is NOT perfect.')

## 숫자형으로 풀어보기