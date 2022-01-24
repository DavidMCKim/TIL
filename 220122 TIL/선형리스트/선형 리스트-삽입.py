## 선형리스트 생성
katok_list = []

## 1-5번째 데이터 입력
katok_list.append(None)
length = len(katok_list)
katok_list[length-1] = '민창'
# print(katok_list)

katok_list.append(None)
length = len(katok_list)
katok_list[length-1] = '희진'
# print(katok_list)

katok_list.append(None)
length = len(katok_list)
katok_list[length-1] = '용수'
# print(katok_list)

katok_list.append(None)
length = len(katok_list)
katok_list[length-1] = '서영'
# print(katok_list)

katok_list.append(None)
length = len(katok_list)
katok_list[length-1] = '현우'
# print(katok_list)

## 선형리스트 삽입 - 희진이 뒤에 지현이를 추가하고싶다면?
katok_list.append(None)
print('기존 리스트\n',katok_list)
length = len(katok_list)
# for i in range(start,end,step) - start = start, end = end-1, step = step
for i in range(length-1,2,-1):
    katok_list[i] = katok_list[i-1]
    katok_list[i-1] = None
print('None을 추가한 리스트\n',katok_list)
katok_list[2] = '지현'
print('2번째 자리에 지현이를 추가한 리스트\n',katok_list)