## 60점
N = int(input())
A_win,B_win = 0,0
for _ in range(N):
    A, B = map(int,input().split(' '))
    if A > B:
        A_win += 1
    elif A < B:
        B_win += 1
print(A_win,B_win)

## 
import sys
N = int(sys.stdin.readline())
A_win,B_win = 0,0
for _ in range(N):
    A, B = map(int,input().split(' '))
    if A > B:
        A_win += 1
    elif A < B:
        B_win += 1
print(A_win,B_win)
