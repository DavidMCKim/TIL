# 31_global_variable_ex.py

def sub(x, y) :
    global a            # 전역변수 : a
    a = 7               # 전역 변수 a 의 값 : 7
    x, y = y, x         # 전역변수 x : 3, y : 4 -> 전역변수 x : 4, y :3
    b = 3               # 지역 변수 b = 3
    print(a, b, x, y)   # 출력값 : 7 3 4 3

a, b, x, y = 1, 2, 3, 4 # 전역 변수 a : 1, b : 2, x : 3, y : 4
sub(x, y)               # 전역변수 a :7 , 전역변수 b : 2, 전역변수 x : 3, 전역변수 y : 4
print(a, b, x, y)       # 출력값 : 7 2 3 4