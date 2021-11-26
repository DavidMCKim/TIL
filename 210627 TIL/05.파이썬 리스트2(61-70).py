# 061 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
print('061')
price = ['20180728', 100, 130, 140, 150, 160, 170]
del price[0]
print(price)
print("---------------------------------")
print()

# 062 슬라이싱을 사용해서 홀수만 출력하라.
print('062')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = nums[0::2]
print(s)
print("---------------------------------")
print()

# 063 슬라이싱을 사용해서 짝수만 출력하라.
print('063')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = nums[1::2]
print(s)
print("---------------------------------")
print()

# 064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
print('064')
nums = [1, 2, 3, 4, 5]
r = nums[4::-1]
print(r)
print("---------------------------------")
print()

# 065 interest 리스트에는 아래의 데이터가 바인딩되어 있다. **
print('065')
interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
# print(interest[::2])
print(interest[0], interest[2])
print("---------------------------------")
print()

# 066 interest 리스트에는 아래의 데이터가 바인딩되어 있다. **
print('066')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
# for i in range(len(interest)) :
#     print(interest[i], end=' ')
print(" ".join(interest))
print("---------------------------------")
print()

# 067 interest 리스트에는 아래의 데이터가 바인딩되어 있다. **
print('067')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print('/'.join(interest))
print("---------------------------------")
print()

# 068 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
print('068')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print('\n'.join(interest))
print("---------------------------------")
print()

# 069 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다. **
print('069')
string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# print(interest)
# ['삼성전자', 'LG전자', 'Naver']
# r = string.replace('/', ',')
r = string.split('/')
print(r)
print("---------------------------------")
print()

# 070 리스트에 있는 값을 오름차순으로 정렬하세요. **
print('070')
data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)
data = sorted(data)
print(data)
print("---------------------------------")
print()