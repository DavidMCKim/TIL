import sys

test = int(sys.stdin.readline().rstrip())

for i in range(test):
    A,B = map(int,input().split(' '))
    print(f'Case #{i+1}: ', A+B)