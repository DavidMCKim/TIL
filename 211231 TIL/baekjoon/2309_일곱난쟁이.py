# for _ in range(9):
#     nanjeng_height = int(input())
print(7+8+10+13+15+19+20)
nanjeng_height = [int(input()) for _ in range(9)]
nanjeng_height.sort()
height_sum = 0
for _ in nanjeng_height:
    print(_)
    height_sum += int(_)
    if height_sum > 100:
        break

