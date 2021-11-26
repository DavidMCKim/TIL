def gugudan(n):
    for i in range(9):
        print(f'{n} * {i+1} = {int(n)*int(i+1)}')

N = int(input())
gugudan(N)
