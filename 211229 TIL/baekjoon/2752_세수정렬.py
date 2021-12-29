A, B, C = map(int,input().split(' '))
list = [A, B, C]
list.sort()
print(list[0], end=' ')
print(list[1], end=' ')
print(list[2])

# print(list) => 오답 : 출력결과를 보니 제일 작은수, 중간수, 제일큰수를 출력하라고 해서 혹시나 했더니..정답..호홋