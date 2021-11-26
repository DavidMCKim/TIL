# 15_list_ex1.py

# 사자성어 맞추기 게임 : 리스트 2개 이용
# 맞출 때 까지 계속
# from random import *
# print('사자성어 맞추기 게임을 시작합니다')
# print('--------------------------------')

# words = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락",
#          "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]
#
# Q = ["잘못을 고치고 옳은 길에 들어섬",
#      "죽일 고비를 여러 번 겪으며 살아나다",
#      "평범한 사람 가운데 뛰어난 사람",
#      "아무짝에나 쓸모 없는 것",
#      "고통과 즐거움을 함께 한다",
#      "미리 준비해두면 근심 걱정이 없다",
#      "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
#      "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
#      "생사를 같이 할 수 있는 친밀한 벗",
#      "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

##############################################
# 내 코드

# use = []
# while True :
#     rand = randint(0,9)
#     while True :
#         for i in range(0,9):
#             print(rand+1,':',Q[rand])
#             num = input('이 말의 사자성어는? : ')
#             if num == words[rand] :
#                 print('맞습니다.. 게임을 종료합니다.')
#                 break
#             else :
#                 print('틀렸습니다...다시 도전 !')
#         break


##############################################
# 강사님 코드

# import random
#
# print('사자성어 맞추기 게임을 시작합니다')
# print('--------------------------------')

# 문제 리스트의 요소 수 범위 (0~9)의 랜덤 숫자 생성이 필요
# 리스트의 인덱스는 0부터 시작
# randrange() 사용해 봄
# i = random.randrange(len(Q)) # 0~9
# i가 문제의 인덱스 번호
# 또한 답의 인덱스 번호

# 맞출 때까지 무한 반복
# 맞추면 반복문 종료

# while True :
#     print(Q[i]) # 랜덤 숫자에 해당되는 문제 출력
#     answer = input('이말의 사자 성어는? : (띄어쓰기 없이 입력)')
#
#     if answer == words[i] :
#         print()
#         print('맞습니다... 게임을 종료합니다.')
#         break
#     else :
#         print()
#         print('틀렸습니다...다시도전 !')
#         print()



# 일회용
# rand = randint(0,9)
# while True :
#     for i in range(0,9):
#         print(rand,'.', Q[rand])
#         num = input('이 말의 사자성어는? : ')
#         if num == words[rand] :
#             print('맞습니다.. 게임을 종료합니다.')
#             break
#         else :
#             print('틀렸습니다...다시 도전 !')
#     break

# 한번씩 다 풀어보기


# use = []
#
# print(type(use))
# for i in range(0,9) :
#     rand = randint(0,9)
#     while True :
#         # for j in range(0,9):
#             print(rand,':',Q[rand])
#             num = input('이 말의 사자성어는? : ')
#             if num == words[rand] :
#                 print('맞습니다.. 게임을 종료합니다.')
#                 for k in use :
#                     if use.count(k) >= 2 :
#                         use.remove(k)
#                 else :
#                     use.append(rand)
#                     print(use)
#                     break
#             else :
#                 print('틀렸습니다...다시 도전 !')
#     break

###################################################3
# rand = randint(0,8)
# use = []
#
# while True :
#     for i in range(0,9):
#         print(Q[rand])
#         print(rand)
#         for j in range(0,i) :
#             if use[j] != rand :
#                 use.append(rand)
#                 print(use)
#         num = input('이 말의 사자성어는? : ')
#         if num == words[rand] :
#             print('맞습니다.. 다음 문제~')
#
#         else :
#             print('틀렸습니다...다시 도전 !')
#     print('다 풀었습니다. 게임을 종료합니다.')
#     break





























import random
from random import *
# import random
# print('사자성어 맞추기 게임을 시작합니다')
# print('--------------------------------')
# sokdam = {'개과천선' : "잘못을 고치고 옳은 길에 들어섬",
#           '구사일생' : '죽일 고비를 여러 번 겪으며 살아나다',
#           '군계일학' : '평범한 사람 가운데 뛰어난 사람',
#           '무용지물' : '아무짝에나 쓸모 없는 것',
#           '동고동락' : '고통과 즐거움을 함께 한다',
#           '유비무환' : '미리 준비해두면 근심 걱정이 없다',
#           '입신양명' : '사회적으로 인정받고 출세하여 이름을 세상에 드날림',
#           '괄목상대' : '다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
#           '막역지우' : '생사를 같이 할 수 있는 친밀한 벗',
#           '고장난명' : '상대 없이 혼자서는 어떤 일을 이룰 수 없다'
# }
import random
from random import *
import random
print('사자성어 맞추기 게임을 시작합니다')
print('--------------------------------')

words = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락",
         "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]

Q = ["잘못을 고치고 옳은 길에 들어섬",
     "죽일 고비를 여러 번 겪으며 살아나다",
     "평범한 사람 가운데 뛰어난 사람",
     "아무짝에나 쓸모 없는 것",
     "고통과 즐거움을 함께 한다",
     "미리 준비해두면 근심 걱정이 없다",
     "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
     "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
     "생사를 같이 할 수 있는 친밀한 벗",
     "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

use = []

def self():
    return -1

while True :
    rand = randrange(len(Q))
    print('%d. : %s' % (rand+1, Q[rand]))
    if rand in use :
        i = self()
        if i == -1 :
            print()
    if rand not in use :
        answer = input('이말의 사자성어는? : ')

        if answer == words[rand] :
            use.append(rand)
            print(use)
            print()
            print('정답입니다~^^다음 문제~~')
            print()
        else :
            print()
            print('틀렸습니다...다시 도전 !')
            print()
# use = []
# while True :
#     rand = randrange(len(Q))
#     while True :
#         for i in range(0,9):
#             print(rand+1,':',Q[rand])
#             num = input('이 말의 사자성어는? : ')
#             if num == words[rand] :
#                 print('맞습니다.. 게임을 종료합니다.')
#                 break
#             else :
#                 print('틀렸습니다...다시 도전 !')
#         break