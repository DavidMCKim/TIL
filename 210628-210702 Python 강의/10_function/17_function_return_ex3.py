# 17_function_return_ex3.py

# 다음의 함수를 포함하는 프로그램 작성
# 함수명 : order()
# 상품가격, 주문수량을 입력 받아서, 주문액을 구하여 반환
#
# def order(p,o) :
#     return p*o
#
# price = int(input('상품가격 입력 : '))
# ord = int(input('주문수량 입력 : '))
# print('-' * 20)
# print('상품가격 : %d원' %price)
# print('주문수량 : %d개' %ord)
# print('주문액 : %d원' %order(price,ord))




def order() :
    pr = int(input('상품가격 입력 : '))
    qt = int(input('주문수량 입력 : '))
    amt = qt * pr
    return pr, qt, amt # 튜플 형태로 반환

# 함수 호출
price, qty, amount = order()

print('-' * 20)
print('상품가격 : %d원' %price)
print('주문수량 : %d개' %qty)
print('주문액 : %d원' %amount)