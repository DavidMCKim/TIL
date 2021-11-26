# 11_list_append_ex3.py

# 80점 이상 학생의 수를 계산하여 출력
# 학생1 점수 입력 : 78
# 학생2 점수 입력 : 91
# 학생3 점수 입력 : 64
# 학생4 점수 입력 : 77
# 학생5 점수 입력 : 83

##############################################
# 내 코드

# score = []
# s = 0
# for i in range(0,5) :
#     student = eval(input('학생%d 점수 입력 : ' %(i+1)))
#     s += student
#     if student >= 80 :
#         score.append(student)
# print('총점 :', s)
# print('평균 : %.2f' %(s/5))
# print('80점 이상 학생 :',len(score),'명')


##############################################
# 강사님 코드

# 빈 리스트 생성
scores = []
for i in range(5) :
    score = int(input('학생'+ str(i+1) +'점수 입력 : '))
    # 리스트에 추가하고
    scores.append(score)

# 누적 변수 생성
sum_s = 0
count = 0 # 80점 이상인 학생 수를 세기 위한 변수
# 리스트의 각 점수 합계
for s in scores :
    sum_s += s # 총점 계산
    if s >= 80 :
        count += 1

# 평균 계산
avg = float(s/len(scores))

# 총점 평균 출력
print('총점 : %d' % sum_s)
print('평균 : %.2f' %avg)
print('80점 이상 학생 : %d명' %count)