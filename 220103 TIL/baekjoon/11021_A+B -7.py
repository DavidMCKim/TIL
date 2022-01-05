# test = int(input())
# c = []
# for i in range(1,test+1):
#     A,B = map(int,input().split(' '))
#     c.append([A,B])
# for i in range(1,len(c)+1):
#     print(f'Case #{i}: ', sum(c[i-1]))

# 도대체 위와 아래의 출력값이 뭐가 다른지 도통 모르겠는 1인....

T = int(input())

for i in range(1,T+1):
    a,b = map(int, input().split())
    print("Case #"+str(i)+':',a+b)