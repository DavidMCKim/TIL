# 21_local_variable.py

# 예제 함수 정의
def show() :
    a = 1 # 함수 내에서 정의된 지역 변수
    a += 1
    print(a) # 변수 a는 함수 내에서만 사용 가능 / 화면에 a변수 값 2를 출력하고 호출한 곳으로 복귀
    # 복귀가 되면 함수는 종료되고 만들었던 모든 변수는 제거

def show1(b) : # 인수가 b에 저장되면서 지역변수 b 생성됨
    b = b+1 # b값을 1 증가
    print(b) # b를 출력 - 함수 종료 - 호출한 곳으로 복귀( 변수 b는 삭제 )

show() # 함수 호출 하면 함수로 이동 후 함수 문장 실행, 실행 종료 후 다시 호출한 곳으로 복귀한다.
# show(a) # a는 현재 파일에서는 함수 내부의 지역변수 이므로 함수 외부에서는 사용불가
# NameError: name 'a' is not defined - a는 함수 내부의 지역변수이기 때문에

show1(20) # 함수 호출 -> 인수를 들고 show1 함수로 이동 후에 인수를 매개변수에 저장 ( 매개변수 생성 ) - 지역 변수
# 복귀 후에는 함수 내 지역변수는 전부 사라짐
# print(b) # 지역변수기 때문에 함수 외부에서는 사용 불가능
# NameError: name 'b' is not defined

# 지역 변수 : 함수 내부에서 생성 되어서 함수 종료 되면 제거되는 변수 / 함수 외부에서는 사용할수 없다.