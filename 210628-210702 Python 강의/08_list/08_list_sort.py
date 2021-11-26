# 08_list_sort.py.py

# sort() : 리스트를 정렬, 원본 리스트 변경
scores = [90, 78, 81, 64, 89] ; print()
scores.sort() # 기본 : 오름차순 정렬
print(scores) # [64, 78, 81, 89, 90]

scores = [90, 78, 81, 64, 89] ; print()
scores.sort(reverse = True) # 내림 차순 정렬
print(scores) # [90, 89, 81, 78, 64]

scores = [90, 78, 81, 64, 89] ; print()
scores.reverse() # 원소의 위치를 역순으로 변경 (정렬은 안함, 가운데 값을 중심으로 좌우가 대칭으로 바뀜)
print(scores) # [89, 64, 81, 78, 90]

## 문자의 정렬 - 대문자 < 소문자, A ~ Z, a ~ z
char = ['b', 'A', 'd', 'C']
char.sort() # 오름차순 정렬
print(char) # ['A', 'C', 'b', 'd']

char = ['b', 'A', 'd', 'C']
char.sort(reverse = True) # 내림차순 정렬
print(char) # ['d', 'b', 'C', 'A']

# 대소문자 구별없이 정렬
# key = str.lower
char = ['b', 'A', 'd', 'C']
char.sort(key = str.lower)
print(char) # ['A', 'b', 'C', 'd']

# 대소문자 구별없이 내림차순 정렬
char = ['b', 'A', 'd', 'C']
char.sort(reverse=True, key=str.lower)
print(char) # ['d', 'C', 'b', 'A']

# 문자열은
ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN']
ids.sort() # 오름차순 정렬 - 첫 문자로 정렬
print(ids) # ['Blue', 'GREEN', 'SKY', 'eBook', 'red']

# 대소문자 구별없이 정렬
ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN']
ids.sort(key=str.lower) # 오름차순 정렬 - 첫 문자로 정렬
print(ids) # ['Blue', 'eBook', 'GREEN', 'red', 'SKY']

# sorted() : 원본 유지하면서 정렬된 새로운 리스트 반환
a = [3, 5, 2, 1, 4]
b = sorted(a)
print('a : ', a)
print('b : ', b)
