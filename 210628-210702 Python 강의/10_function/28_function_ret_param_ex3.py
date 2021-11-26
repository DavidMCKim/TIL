# 28_function_ret_param_ex3.py
# 다음과 같은 함수를 포함하는 프로그램 작성
# 함수명 : order()

def order():

        price = eval(input('상품 가격 입력 : '))
        qty = eval(input('주문 수량 입력 : '))

        amt = price * qty

        if amt >= 100000 :
            d = 0.1
        elif amt >= 50000 :
            d = 0.05
        else :
            d = 1
        dct = amt * d

        tot = amt - dct

        return amt, dct, tot

amount, discount, total = order()

print('-'*30)
print('주문액 : %d원' %amount)
print('할인액 : %d원' %discount)
print('지불액 : %d원' %total)





