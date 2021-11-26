# 20_function_keyward_args.py

# 키워드 인수 예제

def student_info(name, age, gender) :
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }

    return student

# 함수 테스트
# 함수 호춠 인수를 넘겨 dict가 제대로 구성되어 반환되는지 출력
print(student_info(name = 'kim', gender = '여자', age = 23)) # 키워드 인수
print(student_info('lee', 20, '남')) # 위치 인수
print(student_info('park', gender = '남', age = 25)) # 위치 인수와 키워드 인수 동시 사용

### 주의 !
# print(student_info(gender = '남', age = 22, 'lee')) # 위치 인수는 키워드 앞에 위치해야 한다.
# SyntaxError: positional argument follows keyword argument

