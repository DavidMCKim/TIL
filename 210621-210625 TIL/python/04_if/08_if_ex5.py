# 사용자가 선택한 도형의 필요 데이터를 입력받아 면적을 구하는 프로그램
########################################
# 강사님 코드

## 1. 사용자가 선택한 도형
choice = input("도형입력 (1: 사각형, 2: 삼각형, 3: 원) : ")
shape = "" #필요변수 생성 후 초기화
## 2. 필요데이터 입력 (도형에 따른 다른 데이터 입력 유도)
if choice =="1" : # 사각형 선택
    w = int(input("가로 입력 : "))
    h = int(input("세로 입력 : "))
    area = w*h ## 3. 면적 계산 (도형에 따른 다른 계산식 사용)
    shape = "사각형"

elif choice == "2" : # 삼각형 선택
    b = int(input("밑변 입력 : "))
    h = int(input("높이 입력 : "))
    area = b*h/2 ## 3. 면적 계산 (도형에 따른 다른 계산식 사용)
    shape = "삼각형"

else : # 원 선택
    r = int(input("반지름 입력 : "))
    PI = 3.141592
    area = r**2*PI ## 3. 면적 계산 (도형에 따른 다른 계산식 사용)
    shape = "원"

print("%s의 면적은 %.2f" %(shape,area))




########################################
# 내 코드
#
# figure = int(input("1: 사각형, 2: 삼각형, 3: 원 : "))
#
# if (figure == 1 ) :
#     hor = eval(input("가로 입력 : "))
#     ver = eval(input("세로 입력 : "))
#     rec = hor * ver
#
#     print("사각형의 면적 = %.2f" %rec)
# elif (figure ==2 ) :
#     hor = eval(input("밑변 입력 : "))
#     ver = eval(input("높이 입력 : "))
#     tri = (hor * ver) / 2
#
#     print("삼각형의 면적 = %.2f" %tri)
#
# else :
#     half = eval(input("반지름 입력 : "))
#     PI = 3.1416
#     cir = half**2*PI
#
#     print("원의 면적 = %.2f" %cir)
#
