# 점수를 입력 받아서 총점과 평균 출력
kor = eval(input( "국어 점수 입력 : "))
eng = eval(input( "영어 점수 입력 : "))
math = eval(input( "수학 점수 입력 : "))

total = kor + eng + math
avg = total / 3

print("총점 : %d" % total)
print("평균 : %.2f" %avg)
