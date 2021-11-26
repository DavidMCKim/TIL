# 변수는 할당해놓고 사용하지 않으면 메모리 공간을 차지하게 됨
# 변수 삭제 명령어 : del

#del 명령어
'''
c_var = 100
print(c_var)
del c_var
print(c_var)
'''
# 코드 블록 주석처리 : ctrl + / (맥에서는 : command + /)

# 문자열 값 저장
# 문자열은 큰따옴표 사용 가능(작은 따옴표도 사용 가능)
# 여러 종류의 따옴표를 사용할 경우 짝을 잘 맞추어 줘야함
name = '홍길동'
std_name = '김철수'
pro_name = '이몽룡"교수"' #'이몽룡"교수"' , "이몽룡'교수'"
# 한 줄 출력
print(name, std_name, pro_name)
# 여러 줄 출력
print(name)
print(std_name)
print(pro_name)

# 문자열을 연결하는 작업을 할 때 : +연산자 사용
# + 연산자의 기능 1.(문자열) n개의 문자열을 합쳐서 출력 2.(숫자) n개의 숫자의 합 출력
address = '서울시 강남구'

print(name, address) # 두 개의 문자열을 각각 출력
print(name + "은" + address +"에 산다.") # 두 개의 문자열을 하나로 합쳐 출력

result = name + "은" + address +"에 산다." # 변수에는 수식이 들어갈 수도 있다.
print(result)

## 문자와 숫자의 결합(연결)
# 값은 숫자형이지만 문자열로 처리해야 할 때는 일시적으로 형태(type)을 변경함
# 숫자 -> 문자 str(변수명)

age = 23
print(name + '은' , str(age),'살 입니다.')
print(5+age)

## 사각형의 면적을 구해서 출력하는 프로그램
# 넓이 : 100
# 높이 : 200
width = 100
height = 200

area = width * height
print("면적 : " + str(area))
print("면적 : ", area)

##연습문제 1
# 변수 선언 후 값 저장하고 출력
# 변수 : name, no, year, grade, average

name = "홍길동"
no = 2016001
year = 4
grade = 'A'
average = 93.5

print("성명 : " + name)
print("학번 : " + str(no))
print("학년 : " + str(year))
print("학점 : " + grade)
print("평균 : " + str(average))



