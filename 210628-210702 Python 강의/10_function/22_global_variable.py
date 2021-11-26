# 22_global_variable.py
# 전역 변수 (global variable)
# 함쉬 외부에서 정의된 변수
# 프로그램 내 모든 곳에서 사용 가능
# 함수 내에서 전역 변수의 값을 변경하려면 global 키워드 사용

a = 1 # 함수 밖에서 정의된 전역변수 a

def show() :
    c = a + b # 전역 변수 a - 모든 곳에서 사용이 가능
    print(a) # 전역 변수 a - 모든 곳에서 사용이 가능
    print(b)
    print(c)

def add() :
    print(a) # 전역 변수 a - 모든 곳에서 사용이 가능
    print(b)

b = 2 # 함수 밖에서 정의된 전역변수 b - 모든 곳에서 사용 가능
# 함수 정의 후에 만들어 졌지만 함수 내부에서 사용 가능

show()
add()
print(a) # 전역변수는 모든 곳에서 사용 가능
print(b) # 함수 내부 / 함수 외부 모든 곳에서 전역 변수 사용 가능
# print(c) # 전역변수가 정의되어 있더라도 사용 전에 정의되어 있어야 함
c = 3
## 전역변수가 정의된 위치는 함수 앞/다음 상관 없음


### 전역변수 특징
# 함수 입장
# 전역변수 : 함수 내부에서 사용할 수 있음
# 함수 정의 후에 전역변수가 만들어 졌어도 사용가능

# 함수 외부에서 전역변수를 이용해서 실행*처리(할 때
# 실행 전에 전역변수가 생성되어 있어야함