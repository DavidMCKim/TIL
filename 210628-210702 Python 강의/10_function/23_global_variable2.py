# 23_global_variable2.py

# 전역변수를 함수 내부에서 변경하려면 ? global 키워드 사용

a = 1 # 함수 밖에서 정의된 전역변수 a

def add() :
    global a # 'a 변수는 전역변수고 함수 내에서 수정할 수도 있다'라는 키워드
    a = a+1
    c = a+b
    # print(a)
    # print(b)
    # print(c)

b = 3 # 함수 밖에서 정의된 전역변수 b - 함수 정의 후 생성되어도 함수 내에서 사용 가능

print('add 함수 호출 전',a)
add()
print('add 함수 1번 호출',a)
add()
print('add 함수 2번 호출',a)