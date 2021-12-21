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
        select = int(input('숫자를 입력해주세요(1:삽입, 2:추출, 3:위치확인, 4:초기화, 5:나가기) : '))

        if select == 1:
            data = input('삽입할 데이터를 입력해주세요. : ')
            enQueue(data)

        elif select == 2:
            pass

        elif select == 3 :
            pass

        elif select == 4:
            pass

        elif select == 5:
            print(queue)
            print('종료합니다')
            break

        else:
            print('잘못된 입력입니다.\n1~5를 입력해주세요.')