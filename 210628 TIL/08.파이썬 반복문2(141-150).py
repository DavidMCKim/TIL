# 141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라.
# 단 부가세는 10원으로 가정한다.
print('141')
리스트 = [100, 200, 300]
for i in 리스트 :
    print(i+10)
print("---------------------------------")
print()

# 142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
print('142')
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트 :
    print('오늘의 메뉴 :', i)
print("---------------------------------")
print()

# 143 리스트에 주식 종목이름이 저장돼 있다.
print('143')
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트 :
    print(len(i))
print("---------------------------------")
print()

# 144 리스트에는 동물이름이 문자열로 저장돼 있다.
print('144')
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i, len(i))
print("---------------------------------")
print()

# 145 리스트에 동물 이름 저장돼 있다.
print('145')
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i[0])
print("---------------------------------")
print()

# 146 리스트에는 세 개의 숫자가 바인딩돼 있다.
print('146')
리스트 = [1, 2, 3]
for i in 리스트 :
    print('3 x',i)
print("---------------------------------")
print()

# 147 리스트에는 세 개의 숫자가 바인딩돼 있다.
print('147')
리스트 = [1, 2, 3]
for i in 리스트 :
    print('3 x',i,'=',3*i)

# for 변수 in 리스트:
#     print("3 x {} = {}".format(변수, 3 * 변수))
print("---------------------------------")
print()

# 148 리스트에는 네 개의 문자열이 바인딩돼 있다.
print('148')
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:] :
    print(i)
print("---------------------------------")
print()

# 149 리스트에는 네 개의 문자열이 바인딩돼 있다.
print('149')
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2] :
    print(i)
print("---------------------------------")
print()

# 150 리스트에는 네 개의 문자열이 바인딩돼 있다.
print('150')
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1] :
    print(i)
print("---------------------------------")
print()
