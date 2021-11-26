# 03_input().py

# input("프롬프트 문자열") -> 입력되는 모든 값은 문자열로 반환
# x = int(input("숫자 1 입력(정수만 입력하세요) : ")) # 실수 형태 입력 시 에러
# y = float(input("숫자 2 입력 : "))
# z = eval(input("숫자 3 입력 : "))
#
# print(type(z))

#수식을 입력해도 변환을 진행
a = eval(input("수식 입력 : "))
print(a)
print(type(a))

