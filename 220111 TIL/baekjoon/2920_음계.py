sound = list(map(int,input().split(' ')))
answer = [num for num in range(1,9)]

if sound == answer:
    print('ascending')

elif sound == sorted(answer,reverse=True):
    print('descending')

else:
    print('mixed')