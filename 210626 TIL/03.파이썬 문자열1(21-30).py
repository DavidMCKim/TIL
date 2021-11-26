# 021 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
print('021')
letters = 'python'
print(letters[0], end=' ')
print(letters[2])
print("---------------------------------")
print()

# 022 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
print('022')
license_plate = "24가 2210"
print(license_plate[-4:])
print("---------------------------------")
print()

# 023 아래의 문자열에서 '홀'만 출력하세요.
print('023')
string = "홀짝홀짝홀짝"
print(string[::2])
print("---------------------------------")
print()

# 024 문자열을 거꾸로 뒤집어 출력하세요.
print('024')
string = "PYTHON"
print(string[::-1])
print("---------------------------------")
print()

# 025 아래의 전화번호에서 하이푼('-')을 제거하고 출력하세요.
print('025')
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print("---------------------------------")
print()

# 026 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace("-",""))
print("---------------------------------")
print()

# 027 url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.**
print('027')
url = "http://sharebook.kr"
u = url.split('.')
print(u[-1])
print("---------------------------------")
print()

# # 028 아래 코드의 실행 결과를 예상해보세요. **
# print('028')
# lang = 'python'
# lang[0] = 'P'
# print(lang)                 # Python
# print("---------------------------------")
# print()

# 029 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
print('029')
string = 'abcdfe2a354a32a'
s = string.replace('a', 'A')
print(s)
print("---------------------------------")
print()

# 030 아래 코드의 실행 결과를 예상해보세요.
print('030')
string = 'abcd'
s = string.replace('b', 'B')
print(s)
print("---------------------------------")
print()