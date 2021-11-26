# 30_function_dic.py

# 다음과 같은 함수를 포함하는 프로그램 작성
# 함수명 : show_info()
# 이름, 학년, 나이, 연락처를 전달 받아서 딕셔너리로 만들어 출력

def show_info(name, year, age, phone) :

    return print({'name' : name, 'year' : year, 'age' : age, 'phone' : phone})


show_info('홍길동', 4, 23, '010-1234-123')

def show_info() :
    name = input()
    year = input()
    age = input()
    phone = input()

    return print({'name' : name, 'year' : year, 'age' : age, 'phone' : phone})
show_info()
#
list = ['홍길동', 4, 23, '010-1234-1234']
def show_info() :
    name = list[0]
    year = list[1]
    age = list[2]
    phone = list[3]
    return print({'name' : name, 'year' : year, 'age' : age, 'phone' : phone})
show_info()
