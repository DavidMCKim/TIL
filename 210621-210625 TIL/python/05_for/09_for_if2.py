# 09_for_if2
# 정수 10개를 사용자로부터 입력받아서 양,음,0의 개수를 출력하는 프로그램


sum1 = 0                                        # 양의 개수
sum2 = 0                                        # 음의 개수
sum3 = 0                                        # 0의 개수

for i in range(1,11) :
    num = int(input("숫자 %d 입력 : " %i))

    if num>0 :
        sum1 += 1
    elif num <0 :
        sum2 += 1
    else :
        sum3 += 1
print('=============================')
print("양의 개수 : %d" % sum1)
print("음의 개수 : %d" % sum2)
print("0의 개수 : %d" % sum3)

