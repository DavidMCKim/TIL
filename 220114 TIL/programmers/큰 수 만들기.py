k = int(input())

number = '1924'
num = ''
num_list = []
index = 0
while len(num) != len(number)-k:
    if len(num) == len(number)-k:
        num_list.append(num)
        num = 0
    else:
