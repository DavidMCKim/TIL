## functions
def isQueueFull(): # 큐가 가득차있는지 확인
    global SIZE, queue, front, rear
    if (front == rear):
        return 'Full'
    else:
        return 'Not Full'

def isQueueEmpty(): # 큐가 비어있는지 확인
    global SIZE, queue, front, rear
    if (rear == SIZE -1):
        return 'Empty'
    else:
        return 'Not Empty'

def enQueue(data): # 삽입
    global SIZE, queue, front, rear
    if (isQueueFull()=='Full'):
        print('큐가 가득 차 있습니다.')
        return
    rear += 1
    queue[rear] = data

def deQueue(): # 추출
    global SIZE, queue, front, rear
    if isQueueEmpty() == 'Empty':
        print('큐가 비어있습니다.')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek(): # front+1 dnlcl 확인
    global SIZE, queue, front, rear
    if isQueueEmpty() == 'Empty':
        print('큐가 비어있습니다.')
        return -1
    return queue[front+1]

def reset():
    global SIZE, queue, front, rear

## vari
SIZE = int(input('큐의 크기를 입력하세요 : '))
queue = [None for _ in range(SIZE)]
front = -1
rear = -1
select = -1

## main
if __name__ == '__main__':
    while select != 5:
        pass