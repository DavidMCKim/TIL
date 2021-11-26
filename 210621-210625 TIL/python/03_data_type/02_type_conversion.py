# 02_type_conversion.py

# int(문자열) : 문자열을 정수로 변환
# float(문자열) : 문자열을 실수로 변환
# str(정수 또는 실수) : 정수 또는 실수를 문자열로 변환

print("나는 현재 " + str(23) + "살 입니다.")
# 정수와 문자열 결합은 안되기 때문에 정수 리터럴을 문자열로 형변환
print("나는 현재 " + str(169.5) + "cm 입니다.")

#--------- 사용자로부터 숫자를 입력받아 100과 더한 결과를 출력하는 프로그램
# 사용자로 부터 키보드를 이용해서 값을 입력받기 : input() - 컴퓨터는 사용자 입력을 대기하는 상태가 됨
# 키보드로 입력되는 모든 데이터는 문자열로 입력이 됨
# 키보드로 입력되는 숫자 데이터로 처리하고자 할 때는 형변환을 진행해야 함

# num = input("숫자를 입력하세요 : ")
# print(type(num))
# print(int(num)+100)
#
# num = int(input('100과 더할 값을 입력하세요 : '))
# print(num+100)

### 실수 입력
x = input("실수 입력 : ")
y = x*3
print(y)

x = float(input("실수 입력 : "))
y = x*3
print(y)

## 정수 -> 실수 (float) / 실수 -> 정수 (int)
print(int(3.56789))

# format()
# 구분자를 삽입해 줌
print(type(format(3546,','))) # -> format을 사용하면 문자열로 바뀜

'''
rest ='123'
rest = int(rest)

rest = format(int(rest), ',')
# rest = int(format(rest,',')로 하면 123에 ,가 들어감으로 인해 rest는 0,123으로 컴퓨터는 ,를 어떤 가중치로 정수형(int)로 바꿔야 하는지 몰라서 에러가 뜸. 다만 float는 실수형이므로 .을 구분할 수 있음
print(rest)
'''