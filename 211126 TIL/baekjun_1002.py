def turet(x1,y1,r1,x2,y2,r2):
    r = pow(pow((x1-x2),2) + pow((y1-y2),2),0.5)
    sum = r1 + r2
    diff = abs(r1-r2)

    if (r == 0):
        if (diff == 0):
            return -1
        else:
            return 0
    elif (r == sum or r == diff):
        return 1
    elif (diff < r and r < sum):
        return 2
    else:
        return 0

test=int(input('테스트 케이스 개수 : '))
for i in range(test):
    a,b,c,d,e,f = map(int, input().split(' '))
    print(turet(a,b,c,d,e,f))