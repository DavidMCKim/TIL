# for _ in range(9):
#     nanjeng_height = int(input())
nanjeng_height = [int(input()) for _ in range(9)]
nanjeng_height.sort()
height_sum = sum(nanjeng_height)
for x in nanjeng_height:
    for y in nanjeng_height[1:]:
        if height_sum - x - y == 100:
            nanjeng_height.remove(x)
            nanjeng_height.remove(y)

            for _ in nanjeng_height:
                print(_)
            break

    if len(nanjeng_height) <= 8:
        break

