# 18_function_ret_param_ex1.py

# 사칙연산 함수 작성
# add()
# sub()
# mul()
# div()
# a = 9
# b = 3
# 2개의 숫자를 전달받아서 연산 결과 반환

# def add(a,b) :
#     return a+b
#
# def sub(a,b) :
#     return a-b
#
# def mul(a,b) :
#     return a*b
#
# def div(a,b) :
#     return a/b
#
# def four(a,b) :
#     return add(a,b), sub(a,b), mul(a,b), div(a,b)
#
# a = 9
# b = 3
# x, y, z, w = four()
#
# print('%s + %s = %s' %(a,b,x))
# print('%s - %s = %s' %(a,b,y))
# print('%s * %s = %s' %(a,b,z))
# print('%s / %s = %s' %(a,b,int(w)))

def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

x = 9
y = 3


print('%s + %s = %s' %(x,y,add(x,y)))
print('%s - %s = %s' %(x,y,sub(x,y)))
print('%s * %s = %s' %(x,y,mul(x,y)))
print('%s / %s = %s' %(x,y,div(x,y)))