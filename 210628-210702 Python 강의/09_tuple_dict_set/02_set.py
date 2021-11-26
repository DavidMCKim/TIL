# 02_set.py

#### 집합 (set)
# 수학의 집합
# 중복되지 않은 항목들이 모인 것
# 집합= { 항목1, 항목2, … , 항목 }

#### 집합의 특징
# 순서가 없다
# 입력되는 순서와 출력되는 순서가 다를 수 있음
# 동일한 요소(값)이 중복될 수 없다
# 인덱스 사용 불가
# 이미 포함되어 있는 요소(값)를  변경할 수 없음
# 요소 추가/삭제는 가능
# 집합 안에 변경 가능한 항목 포함할 수 없음
# 리스트 포함할 수 없음
# 튜플은 포함 가능
# 튜플은 변경 불가하기 때문

# 집합 만들기 : {} 이용
s1 = {1, 2, 3, 4, 5}
print(s1)
print(type(s1))

# set() 함수로 집합 만들기
s2 = set([10, 20, 30]) # 리스트 -> set 형으로 형변환
print(s2) # {10, 20, 30}
print(type(s2)) # <class 'set'>

s3 = set((100, 200, 300)) # 튜플 -> set 형으로 변환
print(s3)
print(type(s3))

print('============================')

s4 = {1, 2, 3, 3, 4} # 중복값을 set에 저장 - 에러나지는 않는다
print(s4) # 저장할 때 중복값은 1번만 저장 {1, 2, 3, 4}

# {}이용해서 리스트를 집합에 추가하면 에러 발생
# s5 = {1, 2, [3, 4]} # TypeError: unhashable type: 'list'
# print(s5)

# 인덱스 사용 불가
# print(s4[0]) # TypeError: 'set' object is not subscriptable

# s6 = {1, 2,{2, 3}}
# print(s6) # TypeError: unhashable type: 'set'

# 집합에 요소 추가, add()
s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}

# 집합에 요소 추가, update()
s.update([5,6])
# s.update(5,6) # TypeError: 'int' object is not iterable
s.update((5,6))
# s.update(5) # TypeError: 'int' object is not iterable

print(s) # {1, 2, 3, 4, 5, 6}

# 요소 제거
s.remove(3)
print(s) # {1, 2, 4, 5, 6}
s.discard(5)
print(s) # {1, 2, 4, 6}

# 없는 요소 삭제 시
# s.remove(10) # 에러
# s.remove(10) # 에러 없음

# 전체 요소 삭제
s.clear()
print(s) # set() : 빈 집합 의미

# 집합 삭제
# del s # s 변수 삭제됨
# print(s) #NameError: name 's' is not defined

# 집합에 in 또는 not in 연산자 사용 가능
s = {1, 2, 3, 4}
print(3 in s)