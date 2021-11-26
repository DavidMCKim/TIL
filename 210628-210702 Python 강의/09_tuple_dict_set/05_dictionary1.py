# 05_dictionary1.py

# 딕셔너리
# 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {키1:값1, 키2:값2, … }
# d = {1:’a’, 2:’b’, 3:’c’}
#
# 딕셔너리의 특징
# 순서가 없다. 따라서, 인덱스로 접근할 수 없다
# 중괄호 {} 사용
# key를 통해서만 접근
# key는 숫자, 문자 다 가능
# key:value 한 쌍을 item이라고 한다
# 쉼표(,)로 item 구분

d = {1:'a'}
print(d)
print(type(d))
print('-'*100)

# 두번째 요소(item) 추가 (key : 2, value : 'b')
d[2] = 'b' # 주의 : 2는 인덱스가 아닌 key를 의
print('-'*100)

# 세번째 item 추가
# key는 문자도 가능
d['test'] = 'valueTest'
print(d)

print('-'*100)
member = {'name':'홍길동', 'phone':'1234-1234', 'birth':'10/15'}
print(member)

# item 추가 : address : 서울
member['address'] = '서울'
print(member)

# 길면 여러 줄로 입력해도 됨
naver = {
    'name' : 'naver',
    'url' : 'www.naver.com',
    'userid' : 'nv',
    'password' : '1234'
}

print(naver)
print('-'*100)

# dict 필수 함수
# 딕셔너리 주요 함수
# 딕셔너리.keys() : key만 추출해서 리스트로 반환 - 형변환 필요
# [1, 2, 3]
# 딕셔너리.values() : value만 추출 리스트로 반환 - 형변환 필요
# [‘a’, ‘b’, ‘c’]
# 딕셔너리.items() :
# (key:value)의 튜플을 추출해서 리스트로 반환 - 형변환 필요
# [(1:’a’), (2:’b’), (3:’3’)]

print(naver.keys()) # key를 리스트 형태로 반환 : dict_keys(['name', 'url', 'userid', 'password'])
print(naver.values()) # value를 리스트 형태로 반환 : dict_values(['naver', 'www.naver.com', 'nv', '1234'])
print(naver.items()) # (key, value) 리스트 형태로 반환 : dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('userid', 'nv'), ('password', '1234')])

print(type(naver.keys())) # <class 'dict_keys'>
print(type(naver.values())) # <class 'dict_values'>
print(type(naver.items())) # <class 'dict_items'>

print('-'*100)

# 리스트로 변환 : list() 함수 사용
to_list = list(naver.keys())
print(to_list)
print(type(to_list))

# 튜플로 변환 : tuple() 함수 사용
to_tuple = tuple(naver.keys())
print(to_tuple)
print(type(to_tuple))

# 딕셔너리 특정 item의 value 참조 : key를 이용
member = {'name':'홍길동', 'phone':'1234-1234', 'birth':'10/15'}
print(member['name'])

print('-'*100)
# key 리스트의 각 요소 출력
for key in naver.keys() : # dict_keys(['name', 'url', 'userid', 'password'])
    print(key)

print('-'*100)
# value값 출력
for value in naver.values() : # dict_values(['naver', 'www.naver.com', 'nv', '1234'])
    print(value)

print('-'*100)
# item 출력
for item in naver.items() : # dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('userid', 'nv'), ('password', '1234')])
    print(item)

print('-'*100)
# key로 value 찾기 : 딕셔너리변서[key] 이용한 접근 / 딕셔너리변수.get()
print(naver['userid'])
print(naver.get('password'))

# 존재하지 않는 경우 : link 키가 없는 경우
# print(naver['link']) # KeyError: 'link'
print(naver.get('link')) # None
print(naver.get('link','없음')) # 없음

# if문에서 get()사용
insert_key = 'link'
if naver.get(insert_key) is None :
    print(insert_key+'에 대한 data가 없습니다.')

# 존재 여부만 확인 : in / not in
print('link' in naver)
print('link' not in naver)

# list/dict/tuple 관련 함수 확인 : dir() 사용
print('-'*100)
# 리스트 함수 확인
my_list = []
print(dir(my_list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
#  '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

my_tuple = ()
print(dir(my_tuple))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  'count', 'index']

my_dictionary = {}
print(dir(my_dictionary))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
