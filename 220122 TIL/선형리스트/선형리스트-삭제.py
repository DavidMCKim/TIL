# 선형리스트 생성
katok_list = ['민창','희진','지현','용수','서영','현우']

# 선형리스트 삭제 - 지현이를 지우려면??
length = len(katok_list)
katok_list[2] = None
print(katok_list)
for i in range(2,length-1):
    katok_list[i] = katok_list[i+1]
    katok_list[i+1] = None
print(katok_list)
del katok_list[-1]
print(katok_list)


