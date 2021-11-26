# 14_if_ex6.py

# 다음과 같이 프로그램 작성
# 상품번호 입력 시 1,2 이외의 숫자 입력하면 프로그램 종료
# 할인액
# 주문액이 백만원 이상 - 10%
# 백만원 미만 50만원 이상 - 5%
# 50만원 미만 할인 없음

name1 = '노트북'
name2 = '디지털카메라'

price1 = 1200000
price2 = 400000

print("**********상품 정보**********")
print('1 %s : %s 원' %(name1,format(price1,',')))
print('2 %s : %s 원' %(name2,format(price2,',')))
print('****************************')

num = int(input('상품번호 입력 : '))
if num == 1 or num == 2 :                                   # 노트북 또는 디지털 카메라를 선택한 경우
    order = int(input('주문 수량 입력 : '))
else :                                                      # 상품 번호를 잘못 누른 경우
    print('잘못 입력하였습니다. 종료합니다.')
print()
print("**********주문 내용**********")

if num == 1 :                                               # 노트북을 고른 경우
    sum = order * price1                                    # 주문액
    if sum >= 1000000:                                      # 주문액이 100만원 이상인 경우 할인율
        dis = 0.1
    elif sum < 1000000 and sum >= 500000:                   # 주문액이 100만원 미만 50만원 이상인 경우 할인율
        dis = 0.05
    else:                                                   # 주문액이 50만원 미만인 경우 할인율
        dis = 0
    Dis = sum * dis                                         # 할인액
    total = sum - Dis                                       # 총 지불액

    print('상품명 : \t\t\t%s' % name1)
    print('가격 : \t\t\t%s 원' % format(price1,','))
    print('주문 수량 : \t\t%d' % order)
    print('주문액 : \t\t\t%s 원' % format(sum,','))
    print('할인액 : \t\t\t%s 원' % format(int(Dis),','))
    print('총지불액 : \t\t%s 원' % format(int(total),','))

elif num ==2 :                                              # 디지털 카메라를 선택한 경우
    sum = order * price2                                    # 주문액

    if sum >= 1000000:                                      # 주문액이 100만원 이상인 경우 할인율
        dis = 0.1
    elif sum < 1000000 and sum >= 500000:                   # 주문액이 100만원 미만 50만원 이상인 경우 할인율
        dis = 0.05
    else :                                                  # 주문액이 50만원 미만인 경우 할인율
        dis = 0
    Dis = sum * dis                                         # 할인액
    total = sum - Dis                                       # 총 지불액

    print('상품명 : \t\t\t%s' % name2)
    print('가격 : \t\t\t%s 원' % format(price2,','))
    print('주문 수량 : \t\t%d' % order)
    print('주문액 : \t\t\t%s 원' % format(sum,','))
    print('할인액 : \t\t\t%s 원' % format(int(Dis),','))
    print('총지불액 : \t\t%s 원' % format(int(total),','))
