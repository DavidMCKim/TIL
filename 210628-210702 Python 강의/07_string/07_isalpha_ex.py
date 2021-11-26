# # 07_isalpha_ex.py
#
# # 그림과 같이 문장을 입력하고
# # 알파벳, 숫자, 스페이스, 기타 개수 출력

# i = input('문장을 입력하세요 : ')
# c_alpha = 0
# c_num = 0
# c_space = 0
# c_etc = 0
# for x in i :
#     if x.isalpha() :
#         c_alpha += 1
#
#     elif x.isdigit() :
#         c_num += 1
#
#     elif x.isspace() :
#         c_space += 1
#
#     else :
#         c_etc += 1
#
# print('알파벳 : %d개' %c_alpha)
# print('숫자 : %d개'%c_num)
# print('스페이스 : %d개' %c_space)
# print('기타 : %d개' %c_etc)

# 강사님 코드

# count 누적 변수 초기화
alphas = digits = spaces = others = 0

# 문장을 입력받는 코드
string = input('문장을 입력하세요 : ')

# 입력된 문장을 하나씩 추출해서 판단하는 코드
for c in string :
    #print(c) # c 변수에 한 문자씩 대입
    if c.isalpha() : # c.isalpha() == True
        alphas  = alphas + 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        spaces += 1
    else :
        others += 1

print('문자 : %d개' %alphas)
print('숫자 : %d개' %digits)
print('공백 : %d개' %spaces)
print('기타 : %d개' %others)