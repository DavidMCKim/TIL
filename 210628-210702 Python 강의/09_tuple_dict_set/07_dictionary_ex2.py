# 07_dictionary_ex2.py

# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성하고
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램


# mean = input(word,'의 뜻 입력 : ') 와 mean = input('%d의 뜻 입력 : ' %word)가 안되는 이유 찾기

# dict = {}
# while True :
#     word = input('영어 단어 등록 (종료는 quit) : ')
#     if word == 'quit' :
#         print('\n')
#         break
#     if word not in dict.keys() :
#         mean = input(word+'의 뜻입력 (종료는 quit) : ')
#         dict[word] = mean
#         print()
#     elif word in dict.keys():
#         print('%s는 이미 등록된 단어 입니다.' % word)
#         print()
#
# while True :
#     search = input('검색할 단어 입력 (종료는 quit) : ')
#     if search == 'quit':
#         print('종료합니다.')
#         break
#     elif search in dict.keys():
#         print(search + '의 뜻은 ' + dict[search] + '입니다.')
#         print()
#     elif search not in dict.keys():
#         print(search + '는 사전에 없는 단어입니다.')
#         print()


#######################################################
# 내 코드


# dict = {}
# while True :
#     word = input('영어 단어 등록 (종료는 quit) : ')
#     if word == 'quit' :
#         print('\n')
#         break
#     if word not in dict.keys() :
#         mean = input(word+'의 뜻입력 (종료는 quit) : ')
#         dict[word] = mean
#         print()
#     elif word in dict.keys():
#         print('%s는 이미 등록된 단어 입니다.' % word)
#         print()
#
# while True :
#     search = input('검색할 단어 입력 (종료는 quit) : ')
#     if search == 'quit':
#         print('종료합니다.')
#         break
#     elif search in dict.keys():
#         print(search + '의 뜻은 ' + dict[search] + '입니다.')
#         print()
#     elif search not in dict.keys():
#         print(search + '는 사전에 없는 단어입니다.')
#         print()



#######################################################
# 강사님 코드

# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성하고
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램

# 입력의 종료 / 단어 검색의 종료 모두 quit 단어를 이용한다
# 사전구성이 끝나면 바로 단어 검색을 진행한다.

# 빈 딕셔너리 생성
# ek_dic = {}
ek_dic = dict() # dict() 함수 호출

# 사전 구성
# 종료조건은 사용자가 quit 단어를 입력했을 때

while True :
    # 단어 등록
    eng = input('\n 영어 단어 등록 (종료는 quit) : ')

    if eng == 'quit' :
        break # 단어등록 종료
    # elif :
    # 단어를 등록시켜달라는 입력
    # - 사전에 단어가 있는 경우 (등록하면 안됨 : 이미 등록된 단어입니다)
    # - 사전에 단어가 없는 경우 (뜻을 입력받아서 등록)
    if eng == 'quit' :
        break # 단어등록 종료
    elif eng not in ek_dic :
        kor = input('%s의 뜻 입력 : '%eng)
        ek_dic[eng] = kor
    else :
        print(('%s는 이미 등록된 단어 입니다.' %eng))

print(ek_dic)

print('사전에서 단어를 검색하세요.')
while True :
    eng = input('검색할 단어 입력 (종료는 quit) : ')
    if eng == 'quit' :
        break
    elif eng in ek_dic : # 입력된 단어가 사전에 있는 경우
        print('%s의 뜻은 %s입니다.' %(eng,ek_dic[eng]))