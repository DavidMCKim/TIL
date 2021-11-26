# 13_list_append_ex4.py

# 상품을 리스트에 추가
# 엔터키 누르면 입력 종료되고 등록된 상품 리스트 출력

# 상품등록 (엔터키 누르면 종료) : 노트북
# 상품등록 (엔터키 누르면 종료) : 마우스
# 상품등록 (엔터키 누르면 종료) : 키보드
# 상품등록 (엔터키 누르면 종료) :
# 등록된 상품 : 노트북 마우스 키보드


# list = []
# for i in range(0,3) :
#     p = input('회원 입력 : ')
#     list.append(p)
# print('회원 명단 : ',end=' ')
# for i in range(0,len(list)) :
#     print(list[i], end=' ')

##############################################
# 내 코드
# p = []
#
# while True :
#     i = input('상품 등록 (엔터키 누르면 종료) : ')
#     if i == '' :
#         print('등록된 상품 :', end=' ')
#         for i in range(0,len(p)) :
#             print(p[i],end=' ')
#         break
#     else :
#         p.append(i)

##############################################
# 강사님 코드

# 빈 리스트 생성
products = []

# 상품명 입력받아 리스트에 저장하는 코드
while True :
    # 입력받기
    product = input('상품 등록 (엔터키 누르면 종료) : ')

    if product == '' : # 종료 검사 코드
        break
    products.append(product)

print('등록된 상품 : ',end='')

for product in products :
    print(product,end=' ')
