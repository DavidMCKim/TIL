# 151 리스트에는 네 개의 정수가 저장돼 있다.
print('151')
리스트 = [3, -20, -3, 44]
for i in 리스트 :
    if i < 0 :
        print(i)
print("---------------------------------")
print()

# 152 for문을 사용해서 3의 배수만을 출력하라.
print('152')
리스트 = [3, 100, 23, 44]
for i in 리스트 :
    if i%3 == 0 :
        print(i)
print("---------------------------------")
print()

# 153 리스트에서 20보다 작은 3이 배수를 출력하라
print('153')
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트 :
    if i < 20 and i%3==0 :
        print(i)
print("---------------------------------")
print()

# 154 리스트에서 세 글자 이상의 문자를 화면에 출력하라
print('154')
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트 :
    if len(i) >= 3 :
        print(i)
print("---------------------------------")
print()

# 155 리스트에서 대문자만 화면에 출력하라 ** .isupper() = 대문자 구별 (== True(1):대문자, == False(0):소문자)
print('155')
리스트 = ["A", "b", "c", "D"]
for i in 리스트 :
    if i.isupper()==1 :
        print(i)
print("---------------------------------")
print()

# 156 리스트에서 소문자만 화면에 출력하라.
print('156')
for i in 리스트 :
    if i.isupper() == 0:
        print(i)
print("---------------------------------")
print()

# 157 이름의 첫 글자를 대문자로 변경해서 출력하라. **단계 구분해서 첫글자,다른글자 구분!!
print('157')
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    first = i[0].upper()
    print(first+i[1:])
print("---------------------------------")
print()

# 158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트 : split() 메서드)
print('158')
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트 :
    i_s = i.split('.')
    print(i_s[0])
print("---------------------------------")
print()

# 159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
print('159')
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트 :
    ic = i.split('.')
    if ic[1] == 'h' :
        print(i)
print("---------------------------------")
print()


# 160 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
print('160')
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트 :
    ic = i.split('.')
    if ic[1] == 'h' or ic[1] == 'c':
        print(i)
print("---------------------------------")
print()
