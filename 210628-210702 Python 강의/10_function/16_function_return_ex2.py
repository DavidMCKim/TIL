# 16_function_return_ex2.py

# 다음의 함수를 포함하는 프로그램 작성
# 함수 이름 : get_area()
# 사각형의 가로길이와 세로길이를 입력 받아 면적을 구하여 반환

# 가로길이 입력 : 10
# 세로길이 입력 : 20
# 사가형의 면적 : 200

# def get_area():
#     width = eval(input('가로길이 입력 : '))
#     depth = eval(input('세로길이 입력 : '))
#     area = width * depth
#     return area
#
# print('사각형의 면적 : ',get_area())



def get_area():
    width = eval(input('가로길이 입력 : '))
    height = eval(input('세로길이 입력 : '))
    area = width * height
    return area # 결과값 반환 : return width * height

# 테스트코드에서 함수 호출해서 값을 반환받아 출력
rect_area = get_area()
print('사각형의 면적 : ',rect_area)