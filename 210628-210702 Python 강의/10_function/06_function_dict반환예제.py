# 06_function_dict반환예제.py

# 함수 정의
# 함수 이름 : get_info()
# 함수 기능 : 사용자로부터 이름과 나이를 입력받아 딕셔너리로 저장하고
# 저장된 딕셔너리 데이터를 반환하는 함수

def get_info() :

    name = input('이름 : ')
    age = input('나이 : ')

    student = {'name':name, 'age':age}
    return student


# 함수 테스트 :
# 함수를 호출하여 반환값을 student_info 에 저장하고
# 저장된 변수 값을 출력/변수의 형태를 확인

student_info = get_info()
print(student_info)
print(type(student_info))