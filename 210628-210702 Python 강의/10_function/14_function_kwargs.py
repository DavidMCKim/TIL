# 14_function_kwargs.py

# 가변길이 매개변수 **kwgrgs
# keyword arguments의 약자, key = value 형태로 값을 받는다.

def show_keywars(**kwargs) : # 인수는 dict 형태로 전달된다.
    print(kwargs)
    print(type(kwargs))

# 함수 호출
show_keywars() # 빈 dict가 전달된다.
show_keywars(a=3)

show_keywars(id='sun',
             name='kim',
             phone='010-1234-1234')

show_keywars(num='3',
             val='kim',
             str='abcdef')