## 메모리 : 49348KB / 시간 : 5616ms
N = int(input())
room = []
t = 0
answer = 0
for i in range(N):
    start,stop = map(int,input().split())
    room.append((start,stop))
room = sorted(room,key=lambda x:x[0])
room = sorted(room,key=lambda x:x[1])
for i in room:
    if i[0] >= t:
        answer += 1
        t = i[1]
print(answer)



## 메모리 : 46280KB / 시간 : 4276ms
N = int(input())
room = []
t = 0
answer = 0
for i in range(N):
    start,stop = map(int,input().split())
    room.append((start,stop))
room = sorted(room,key=lambda x:x[0])
room = sorted(room,key=lambda x:x[1])
for i,j in room:
    if i >= t:
        answer += 1
        t = j
print(answer)