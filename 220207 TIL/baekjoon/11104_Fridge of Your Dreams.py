n = int(input())
for i in range(n):
    e_jinsu = list(input())
    e_jinsu.reverse()
    decimal_number = []
    for index,num in enumerate(e_jinsu):
        if num == '1':
                decimal_number.append(2 ** index)
    print(sum(decimal_number))