# 04_function_return_multi.py

# 여러개의 값 반환하기
# 파이썬을 제외한 다른 프로그래밍 언어에서는 함수는 항상 하나의 값만 반환
# 파이썬에서는 함수가 여러 개의 값을 반환 할 수 있음

def multi_return() :
    return 1,2,3
    # return 1 # 1 반환하고 호출한 곳으로 포커스가 넘어감
    # return 2 # 실행되지 않음
    # return 3 # 실행되지 않음

a, b, c = multi_return() # 반환된 여러개의 값을 변수에 저장 -> 여러 변수에 저장해야 함
print('여러 변수에 저장 후 출력')
print(a,b,c)

print('반환된 값을 바로 출력')
print(multi_return()) # (1,2,3) - 튜플로 반환
print(type(multi_return())) # (1,2,3) - <class 'tuple'>