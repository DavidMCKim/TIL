import math
n = int(input())
if n == 2:
    a,b = map(int,input().split())
    gcd = math.gcd(a,b)
    for i in range(1,gcd+1):
        if a%i ==0 and b%i ==0:
            print(i)
elif n == 3:
    a,b,c = map(int,input().split())
    gcd = math.gcd(a, b)
    for i in range(1,gcd+1):
        if a%i ==0 and b%i ==0 and c%i == 0:
            print(i)