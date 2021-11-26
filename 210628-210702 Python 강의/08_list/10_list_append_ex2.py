# 10_list_append_ex2.py

# 학생 5명의 점수를 입력 받아서 list에 저장한 수 총점과 평균ㅇ르 구하여 출력

# 학생1 점수 입력 : 90
# 학생2 점수 입력 : 87
# 학생3 점수 입력 : 68
# 학생4 점수 입력 : 79
# 학생5 점수 입력 : 92
# 총점 : 416
# 평균 83.20


##############################################
# 내 코드

# append 사용한 코드

score = []
s = 0
for i in range(0,5) :
    student = eval(input('학생%d 점수 입력 : ' %(i+1)))
    score.append(student)
    s += score[i]

print('총점 :', s)
print('평균 : %.2f' %(s/5))

##############################################
# 강사님 코드

# 빈 리스트 생성
scores = []
for i in range(5) :
    score = int(input('학생'+ i+1 +'점수 입력 : '))
    # 리스트에 추가하고
    scores.append(score)

# 누적 변수 생성
sum_s = 0
# 리스트의 각 점수 합계
for s in scores :
    sum_s += s # 총점 계산

# 평균 계산
avg = float(s/len(scores))

# 총점 평균 출력
print('총점 : %d' % sum_s)
print('평균 : %.2f' %avg)