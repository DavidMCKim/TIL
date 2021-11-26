# 09_list_append_ex1.py

# 3명의 회원을 입력 받아 리스트에 추가하고, 리스트 내용 출력 (for 문 사용)

##############################################
# 내 코드
# list = []
# for i in range(0,3) :
#     p = input('회원 입력 : ')
#     list.append(p)
# print('회원 명단 : ',end=' ')
# for i in range(0,len(list)) :
#     print(list[i], end=' ')

##############################################
# 강사님 코드

# 빈 리스트 생성
members = []
for i in range(5) :
    member = input('회원 입력 : ')
    # 리스트에 추가하고
    members.append(member)

# 리스트 내용 출력
print('회원 명단 : ',end='')
for member in members :
    print(member,end=' ')