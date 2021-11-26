# 101 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
print('101')
print(bool)
print("---------------------------------")
print()

# 102 아래 코드의 출력 결과를 예상하라.
print('102')
print(3 == 5) # False
print("---------------------------------")
print()

# 103 아래 코드의 출력을 예상하라.
print('103')
print((3 < 5)) # True
print("---------------------------------")
print()

# 104 아래 코드의 결과를 예상하라.
print('104')
x = 4
print(1<x<5)    #True
print("---------------------------------")
print()

# 105 아래 코드의 결과를 예상하라.
print('105')
print((3 == 3) and (4 != 3))    # True
print("---------------------------------")
print()

# 106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
print('106')
print('3 => 4')
print('부등호와 등호의 순서가 바뀌었다. ')
print("---------------------------------")
print()

# 107 아래 코드의 출력 결과를 예상하라
print('107')
if 4<3 :
    print('Hello World')
print('아무것도 출력되지 않는다.')
print("---------------------------------")
print()

# 108 아래 코드의 출력 결과를 예상하라.
print('108')
if 4<3 :
    print('Hello World')
else :
    print('Hi, there.')
print('Hi, there.')
print("---------------------------------")
print()

# 109 아래 코드의 출력 결과를 예상하라
print('109')
if True :
    print('1')
    print('2')
else :
    print('3')
print('4')
print('1\n2\n4')
print("---------------------------------")
print()

# 110 아래 코드의 출력 결과를 예상하라
print('110')
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
print('3\n5')
print("---------------------------------")
print()