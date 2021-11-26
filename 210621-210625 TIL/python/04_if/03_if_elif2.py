# 03_if_elif2.py

# 사용자로부터 점수를 입력받아서 학점을 구하는 프로그램



jumsu = eval(input("당신의 점수를 입력하세요 : "))

if jumsu >= 90 :
    print("A")
elif jumsu >= 80 :
    print("B")
elif jumsu >= 70 :
    print("C")
elif jumsu >= 60 :
    print("D")
else :
    print("F")