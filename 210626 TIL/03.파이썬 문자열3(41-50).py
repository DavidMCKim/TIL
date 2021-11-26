# 041 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
print('041')
ticker = 'btc_krw'
t = ticker.upper()
print(t)
print("---------------------------------")
print()

# 042 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
print('042')
t1 = ticker.lower()
print(t1)
print("---------------------------------")
print()

# 043 문자열'hello'가 있을 때 이를 'Hello'로 변경해보세요.
print('043')
i = 'hello'
ic = i.replace('h', 'H')

print(ic)
print("---------------------------------")
print()

# 044 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요. **
# 정의된 문자열이 지정된 접미사로 끝나면 True를 돌려주고, 그렇지 않으면 False를 돌려줍니다.
# 접미사는 찾고자 하는 접미사들의 튜플이 될 수 도 있습니다. 선택적 start가 제공되면 그 위치에서 검사를 시작합니다. 선택적 end를 사용하면 해당위치에서 비교를 중단합니다.
# str.endswith(접미사[, start [,end]])
print('044')
file_name = '보고서.xlsx'
print(file_name.endswith('xlsx'))
print("---------------------------------")
print()

# 045 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
print('045')
file_name = '보고서.xlsx'
# print(file_name.endswith('xlsx' or 'xls'))
print(file_name.endswith(('xlsx', 'xls')))
print("---------------------------------")
print()

# 046 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
print('045')
file_name = '2020_보고서.xlsx'
print(file_name.startswith("2020"))
print("---------------------------------")
print()

# 047 다음과 같이 문자열이 있을 때 공북앨 기준으로 문자열을 나워보세요.
print('047')
a = "hello world"
a1 = a.split()
print(a1)
print("---------------------------------")
print()

# 048 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
print('047')
ticker = 'btc_krw'
t = ticker.split('_')
print()
print("---------------------------------")
print()

# 049 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
print('049')
data = '2020-05-01'
d = data.split('-')
print(d)
print("---------------------------------")
print()

# 050 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요. **
# rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다.
# 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제됩니다.
print('050')
data = '039490            '
# d = data.strip()
d = data.rstrip()
print(d)
print("---------------------------------")
print()

# # lstrip 예제
# print('051')
# data = '              3939'
# d = data.lstrip()
# print(d)