# # 06_dictionary_ex1.py
#
# # 다음과 같이 리스트를 선언하고 각 학생의 총점과 평균 출
#
# #######################################################
# # 내 코드
# student = [
#     {'name' : '홍길동', 'korean' : 87, 'math' : 98, 'english' : 88, 'science' : 95},
#     {'name' : '이몽룡', 'korean' : 92, 'math' : 98, 'english' : 96, 'science' : 98},
#     {'name' : '성춘향', 'korean' : 76, 'math' : 96, 'english' : 94, 'science' : 90},
#     {'name' : '변학도', 'korean' : 98, 'math' : 92, 'english' : 96, 'science' : 92},
#     {'name' : '박지성', 'korean' : 95, 'math' : 98, 'english' : 98, 'science' : 98},
#     {'name' : '류현진', 'korean' : 64, 'math' : 88, 'english' : 92, 'science' : 92},
# ]
#
#
# print('이름\t\t\t 총점\t\t\t  평균')
# for i in range(6):
#     sum = student[i]['korean'] + student[i]['math'] + student[i]['english'] + student[i]['science']
#     avg = sum / (len(student[i])-1)
#     print(student[i]['name'],'\t\t',sum,'\t\t\t',avg)



#######################################################
# 강사님 코드
students = [
    {'name' : '홍길동', 'korean' : 87, 'math' : 98, 'english' : 88, 'science' : 95},
    {'name' : '이몽룡', 'korean' : 92, 'math' : 98, 'english' : 96, 'science' : 98},
    {'name' : '성춘향', 'korean' : 76, 'math' : 96, 'english' : 94, 'science' : 90},
    {'name' : '변학도', 'korean' : 98, 'math' : 92, 'english' : 96, 'science' : 92},
    {'name' : '박지성', 'korean' : 95, 'math' : 98, 'english' : 98, 'science' : 98},
    {'name' : '류현진', 'korean' : 64, 'math' : 88, 'english' : 92, 'science' : 92},
]

print()

# 타이틀 출력
print('이름', '\t 총점', '\t  평균')

for s in students :
    std_sum = s['korean'] + s['math'] + s['english'] + s['science']
    std_avg = std_sum / 4

    print(s['name'], '\t', std_sum, '\t', std_avg)