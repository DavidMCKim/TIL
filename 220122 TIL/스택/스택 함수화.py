## function
def isStackEmpty():  # 비어있는지 확인
    global SIZE, stack, top
    if (top == -1):
        return 'Empty'
    else :
        return 'Not Empty'

def isStackFull():  # 꽉 차 있는지 확인
    global SIZE, stack, top
    if top >= SIZE-1:
        return 'Full'
    else:
        return 'Not Full'

def push(data): # 삽입
    global SIZE, stack, top
    if isStackFull() == 'Full':
        print('스택이 비어있지 않습니다.')
        return
    top += 1
    stack[top] = data

def pop(): # 추출
    global SIZE, stack, top
    if isStackEmpty() == 'Empty':
        print('스택이 비어있습니다.')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek(): # top 위치의 데이터 확인
    global SIZE, stack, top
    if (isStackEmpty()=='Empty'):
        print('스택이 비어있습니다.')
        return -1
    return stack[top]

def reset(): # 초기화
    global stack, SIZE, top
    for item in range(SIZE-1,-1,-1):
        stack[item] = None
        top -= 1

## vari
SIZE = 5
stack = [None,None,None,None,None]
top = -1
select = -1

## main
if __name__ == '__main__':

    while select != 5:
        select = int(input('입력하세요(1:push, 2:pop, 3:peek, 4:reset, 5:end ) : '))
        if select == 1:
            data = input('삽입할 데이터를 입력하세요 : ')
            push(data)
            print('스택 -->',stack)

        elif select == 2:
            pop()
            print('추출한 데이터 -->', data)
            print('스택 -->', stack)

        elif select == 3:
            data = peek()
            print('top 위치 :', data)
            print('스택 -->', stack)

        elif select == 4:
            reset()
            print('스택 -->', stack)

        elif select == 5:
            print('최종 스택 -->',stack)
            print('종료되었습니다.^^')
            break

        else:
            print('잘못된 입력입니다ㅠㅠ \n1~4중에서 입력해주세요(1:push, 2:pop, 3:peek, 4:end)')