# # 01_slicing.py
#
# # 문자열
# # 문자의 나열 - 여러 문자로 이루어져 있기 때문에 한문자당 하나의 메모리 공간을 차지한다
# # 'abc' -> a한칸 b한칸 c한칸의 공간을 차지하고 공간이 연속되어 있음
#
# # 인덱싱과 슬라이싱이 가능
#
# # 문자열 생성 - '', "", """ """
# crawling = 'Data crawling is fun'
# parsing = 'Data parsing is also fun'
#
# # 전체 문자열 출력 (반환)
# print(crawling)
# print(crawling[:])
#
# # 특정 인덱스의 문자 출력 - 파이썬의 인덱싱은 0부터 시작함
# print(crawling[0])              # 첫 번째 문자
# print(crawling[-1])             # 마지막 문자
# print(crawling[2])
#
# # 슬라이싱 예제
# print(crawling[0:4])            # 0~3 번 인덱스 까지
# print(crawling[5:16])           # 5~15번 인덱스 까지
# print(crawling[17:])            # stop을 생략하면 끝까지 - 17 ~ 끝까지
# print(crawling[19])             # 인덱스 19번 문자
# print(crawling[-1:])            # 시작은 마지막 문자에서 끝까지 - 마지막 문자
# print(crawling[-1])             # 위 코드와 같은 결과
# print(crawling[:-1])            # 처음부터 마지막 전 문자까지
# print(crawling[16:16+4])        # 16:20 과 동일 16~19까지
#
# print('----------------------------------')
#
# print(parsing)                  # 전체 출력
# print(parsing[5:])              # parsing is also fun
# print(parsing[:15])             # Data parsing is
# print(parsing[:])               # Data parsing is also fun
#
#### 주의 ####

string = 'happy day!!!'

string_a = string[:5] # 가능
print(string_a)

string[:5] = 'abc' # 문자열 변수의 부분 수정은 불가능
# print(string)
string = 'abc12' # 문자열변수 전체 수정은 가능
print(string)