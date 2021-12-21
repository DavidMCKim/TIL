## functions
def isQueueFull():
    global size, queue, front, rear
    if (rear+1) % size == front:
        return True
    else:
        return False

def isQueueEmpty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front, rear
    if isQueueFull():
        print('큐가 가득 차 있습니다.')
        return
    rear = (rear+1) % size
    queue[rear] == data


def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print('큐가 비어있습니다.')
        return
    front = (front+1) % size
    data = queue[front]
    queue[front] = None
    return data

def peek():
    if isQueueEmpty():
        print('큐가 비어있습니다.')
        return 0
    return queue[(front+1)%size]

## vari
size = int(input('원형 큐의 크기를 입력하세요 : '))
queue = [None for _ in range(size)]
print(queue)
front = -1
rear = -1
select = -1

## main
if __name__ == '__main__':

    while select != 4:
        select = int(input('숫자를 입력해주세요(1:삽입, 2:추출, 3:위치확인, 4:초기화, 5:나가기) : '))

        if select == 1:
            data = input('삽입할 데이터를 입력해주세요. : ')
            enQueue(data)
            print('현재 큐 : ', queue)
            print(f'front: {front} \nrear : {rear}')

        elif select == 2:
            data = deQueue()
            print('추출된 데이터 : ', data)
            print('현재 큐 : ', queue)
            print(f'front: {front} \nrear : {rear}')

        elif select == 3:
            data = peek()
            print('가장 먼저 나갈 데이터 위치 : ', data)
            print('현재 큐 : ', queue)
            print(f'front: {front} \nrear : {rear}')

        elif select == 4:
            print('최종 큐 : ', queue)
            print('종료합니다')
            print(f'front: {front} \nrear : {rear}')
            break

        else:
            print('잘못된 입력입니다.\n1~4를 입력해주세요.(1:삽입, 2:추출, 3:위치확인, 4:나가기)')