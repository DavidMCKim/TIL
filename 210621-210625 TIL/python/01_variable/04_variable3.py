## print()함수에서 문자열과 변수를 함꼐 출력할 때
# 방법 1
# print("문자열",변수)
# 방법 2 : 포멧 코드 사용
# print("서식" % 값)
# print("문자열 %d 문자열" % 변수)
# print("나이 : %D 살" % age)
# print("내 이름은 %s 입니다" %name)

## 포맷코드 사용
# 문자열 : %s
# 정수 : %d
# 실수 : %f
# 문자하나 : %c

name = "홍길동"
no = 2016001
year = 4
grade = 'A'
average = 93.5
level = 10

print("성명 : %s" %name)
print("학번 : %d" %no)
print("학년 : %d" %year)
print("학점 : %c" %grade)
print("평균 : %.2f" %average)
print("등급 : %d %%" %level) # %문자를 사용하고 싶으면 %%

# 화씨 온도를 섭씨 온도로 변환
fTemp = 90 # 정수 변수
cTemp = (fTemp - 32) * 5 / 9 # 정수 연산

# cTemp 변수에 type은?
print(cTemp)
print("%f" %cTemp)
print("%.3f" %cTemp)
print("%10.3f" %cTemp) # 실수 %f 사용시 %전체자리수.소수이하자리수f

# 포멧 코드 사용 시 n개의 코드 사용할 때 ()로 묶어서 사용
print("화씨온도 %d를 섭씨 온도로 변환하면 %.3f 입니다." %(fTemp, cTemp))

