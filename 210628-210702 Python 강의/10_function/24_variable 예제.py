# 24_variable 예제.py

def sub(x,y) : # 매개변수 x,y -> 지역변수 x -> 3, y -> 4
    global a
    a = 7 # 전역변수 a가 7로 수정
    x,y = y,x # x와 y는 지역변수를 사용 : x->4 , y->3
    b = 3 # 지역변수 정의
    print(a,b,x,y) # 출력되는 값을 예측 a -> 7, b -> 3, x ->4, y -> 3 (출력 : 7 3 4 3)

a,b,x,y = 1,2,3,4 # a,b,x,y -> 전역변수
sub(x,y)
print(a,b,x,y) # 출력되는 값을 예측 : a -> 7, b -> 2, x-> 3, y-> 4 (출력 : 7 2 3 4)

# 전역변수 a가 생성되어 있어도 지역변수 a를 생성해서 함수 내부에서 사용 가능

def test(a,b) : # 매개변수 a -> 5, b -> 6
    x = 10 # x는 지역변수
    print(y)
    a = 3 # a는 지역변수 수정
    b = 5 # b는 지역변수 수정
    print(x, y, a, b) # y는 전역변수를 사용 # 출력값 : 10 10 3 5

a = 5
b = 6
x = 9
y = 10
a = x*y
test(a,b)
print(x, y, a, b) # 출력값 : 9 10 90 6