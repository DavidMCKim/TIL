from sys import*
from collections import*
input = lambda:stdin.readline().strip()
def cal2(n1, op, n2):    #연산 받아서 계산
   if op == '+': return n1+n2
   if op == '-': return n1-n2
   if op == '*': return n1*n2
def cal():
   q=deque()                        #deque 사용
   i=0
   while 1:                         #괄호 먼저 처리
       if i==n: break
       if i%2 != 0 and check[i]:    #수식 자리이고, check 켜져있으면(괄호이면)
           q.append(cal2(int(q.pop()), a[i], int(a[i+1])))    #계산해서 넣어줌
       else:                        #수식이 아니거나 안켜져 있으면 그냥 넣어줌
           q.append(a[i])
       i+=1
   while q:                         #괄호 처리가 완료된 수식 처리
       if len(q)==1: break          #q에 숫자 하나만 있으면 끝
       q.appendleft(cal2(int(q.popleft()), q.popleft(), int(q.popleft())))
   return q[0]
def solve(pos=1):                    #완탐
   global res
   if pos >= n:return cal()         #n개 이상=> 끝에 다다름, 계산해줌
   check[pos]=1
   res = max(res, solve(pos+4))     #수식을 선택했으면, 다다음 수식으로(문제에 괄호 겹치지 말라고 주어짐)
   check[pos]=0
   res = max(res, solve(pos+2))     #주어진 문자열에서 수식 2칸씩 띄어져 있음
   return res
n=int(input())
res=int(-1e10)
check=[0]*n
a=input()
print(solve())