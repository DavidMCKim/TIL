# 29_function_gbb_game.py

from random import *

def gbb_game() :
    for i in range(4):
        com = randint(1,3)
        you = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))

        if (you == 1 and com == 3) or (you == 2 and com == 1) or (you == 3 and com == 2) :
            print('당신이 이겼습니다.')
            print(com)
        elif (you == com) :
            print('비겼습니다.')
            print(com)
        else :
            print('컴퓨터가 이겼습니다.')
            print(com)

gbb_game()