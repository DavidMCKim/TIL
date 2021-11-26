# 13_random_가위바위보
# 홍길동과 컴퓨터 간의 가위바위보 게임

# # 랜덤 모듈 가져오기
from random import randint

#사용자 가위바위보 데이터 입력 받기
hong = input('홍길동 입력 : ')
# 난수 발생 : 1.가위 2.바위 3.보
com = randint(1,3)
if com ==1 :
    com = '가위'
elif com == 2:
    com = '바위'
else :
    com = '보'
# 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성
if (hong == '가위' and com == '보') or (hong == '바위' and com == '가위') or (hong == '보' and com == '바위') :
    print(com)
    print('홍길동님이 이겼습니다.')
elif (hong == com) :
    print(com)
    print('비겼습니다.')
else :
    print(com)
    print('컴퓨터가 이겼습니다.')


# # 랜덤 모듈 가져오기
# from random import randint
#
# # 사용자 이름 입력
# name = input("사용자 이름 : ")
#
# while 1 :
#     #사용자 가위바위보 데이터 입력 받기
#     user = input('%s입력 : ' %name)
#     # 난수 발생 : 1.가위 2.바위 3.보
#     com = randint(1,3)
#     if com ==1 :
#         com = '가위'
#     elif com == 2:
#         com = '바위'
#     else :
#         com = '보'
#     # 홍길동이 이기는 모든 경우의 수를 if 조건으로 생성
#     if (user == '가위' and com == '보') or (user == '바위' and com == '가위') or (user == '보' and com == '바위') :
#         print('%s님이 이겼습니다.' %name)
#     elif (user == com) :
#         print('비겼습니다.')
#     else :
#         print('컴퓨터가 이겼습니다.')