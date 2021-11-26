
cnt = int(input('테스트 케이스 개수 : '))
A = []
for i in range(cnt):
    x1, y1, r1, x2, y2, r2 = map(int,input().split(' '))
    r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)


    A.append(-1 if (r == 0 and r1 == r2) else 0 if (abs(r1-r2) < r < (r1+r2)) else 1 if (abs(r1-r2) == r) else 2)

for i in A:
    print(i)



