# 다음과 같이 무게와 키 값을 입력 받아서 BMI 지수를 계산하는 프로그램 작성
# BMI = 몸무게 / 키의 제곱

weight = eval(input( "몸무게(킬로그램): "))
height = eval(input( "키(미터): "))

bmi = weight / height**2

# print("당신의 BMI : %.2f" %bmi)

# format() 함수 사용
print("당신의 BMI : ", format(bmi, '.2f'))