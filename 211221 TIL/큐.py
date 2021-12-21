## functions
def isQueueFull(): # 큐가 가득차있는지 확인
    global size, queue, front, rear
    if rear != size-1:
        return False
    if rear == size -1 and front == -1:
        return True
    else:
        for i in range(front+1, size):
            queue[i-1] = i
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty(): # 큐가 비어있는지 확인
    global size, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data): # 삽입
    global size, queue, front, rear
    if isQueueFull():
        print('큐가 가득 차 있습니다.')
        return
    rear += 1
    queue[rear] = data

def deQueue(): # 추출
    global size, queue, front, rear
    if isQueueEmpty():
        print('큐가 비어있습니다.')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek(): # front+1 위치 확인
    global size, queue, front, rear
    if isQueueEmpty() == 'Empty':
        print('큐가 비어있습니다.')
        return -1
    return queue[front+1]

## vari
size = int(input('큐의 크기를 입력하세요 : '))
queue = [None for _ in range(size)]
print(queue)
front = -1
rear = -1
select = -1

## main
if __name__ == '__main__':
    while select != 4:
        select = int(input('숫자를 입력해주세요(1:삽입, 2:추출, 3:위치확인, 4:나가기) : '))

        if select == 1:
            data = input('삽입할 데이터를 입력해주세요. : ')
            enQueue(data)
            print('현재 큐 : ', queue)

        elif select == 2:
            data = deQueue()
            print('추출된 데이터 : ', data)
            print('현재 큐 : ', queue)

        elif select == 3 :
            data = peek()
            print('가장 먼저 나갈 데이터 위치 : ', data)
            print('현재 큐 : ', queue)

        elif select == 4:
            print('최종 큐 : ', queue)
            print('종료합니다')
            break

        else:
            print('잘못된 입력입니다.\n1~4를 입력해주세요.')