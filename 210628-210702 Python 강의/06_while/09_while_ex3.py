# # 09_while_ex3.py
#
# # 사용자에게 숫자(정수)를 입력받아 '홀수'이면 아래 예시와 같이 출력하고 '짝수'이면 출력 없이 다음 입력을 받는 프로그램을 작성하시오.
# # 종료는 입력에 x문자가 들어오면 종료하되 break 문을 활용하고,
# # 짝수일 경우 출력의 건너뜀은 continue문을 활용해 보시오
#
#
# ###########################################
# # 내 코드
while True :
    num = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
    if num == 'x' :
        break
    else :
        i = int(num)
        if i %2 == 0 :
            continue
        else :
            print('%d는 홀 수 입니다. '%i)
#
# ###########################################
# # 강사님 코드
#
# while True :
#     s = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
#
#     if s == 'x' :
#         print('종료합니다.')
#         break
#
#     if int(s) %2 == 0 :
#         continue
#
#     print(s+'는 홀수입니다.')
#
#
# ###########################################
# # 정문님 코드
#
# while True:
#     num = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
#     print(int(num))
#
#     if int(num) %2 == 0 :
#         continue
#     elif num == 'x':
#         break
#
#
#     print('%d는 홀 수 입니다.' %int(num))
#     continue
#     # break
# print('종료합니다.')
#
###########################################
# 새봄님 코드
# while True :
#     num = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
#     if num == 'x' :
#         print('종료합니다.')
#         break
#     elif int(num) %2 == 1 :
#         print("%d는 홀수입니다." % int(num))
#         # break
#     else :
#         continue