# 14_list_sort_ex.py

# append() 연습문제2 (10_list_append_ex2.py) 복사해서 점수를 내림차순 정렬하여 출력

##############################################
# 내 코드
# score = []
# s = 0
# c = []
# count = int(input('학생 수 입력 : '))
# for i in range(0,count) :
#     student = eval(input('학생%d 점수 입력 : ' %i))
#     c.append(student)
#     s += student
#     if student >= 80:
#         score.append(student)
# print('총점 :', s)
# print('평균 : %.2f' % (s / count))
# print('80점 이상 학생 :', len(score), '명')
# c.sort()
# print(c)

##############################################
# 강사님 코드

# 학생 수 입력 받는 코드
num = int(input('학생 수 입력 : '))
# 빈 리스트 생성
scores = []
for i in range(num) :
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

# scores 정렬
scores.sort(reverse=True) # 내림차순 정렬
print('점수 내림차순 정렬 : ', scores)