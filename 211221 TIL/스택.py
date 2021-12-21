## functions
def isStackFull(): # 스택이 가득 차 있는지 확인
    global size, stack, top
    if top >= size-1:
        return True
    else:
        return False

def isStackEmpty(): # 스택이 비어있는지 확인
    global size, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data): # 데이터 삽입
    global size, stack, top
    if isStackFull():
        print('스택이 가득 차 있습니다.')
        return
    top += 1
    stack[top] = data
    return stack

def pop(): # 데이터 추출
    global size, stack, top
    if isStackEmpty():
        print('스택이 비어있습니다.')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek(): # top 위치 확인
    global size, stack, top
    if isStackEmpty():
        print('스택이 비어있습니다.')
        return -1
    else:
        return stack[top]

## vari
size = int(input('스택의 사이를 입력하세요. : '))
stack = [None for _ in range(size)]
print(stack)
top = -1
select = -1

## main
if __name__ == '__main__':
    while select != 'X' and select != 'x':
        select = input('삽입(I) / 추출(E) / 확인(Y) / 종료(X) 중 입력 : ')
        if select == 'I' or select == 'i':
            data = input('삽입할 데이터 : ')
            push(data)
            print('현재 스택 --> ',stack)

        elif select == 'E' or select == 'e':
            data = pop()
            print('추출할 데이터 : ',data)
            print('현재 스택 --> ',stack)

        elif select == 'Y' or select == 'y':
            current_top = peek()
            print('top의 위치 : ', current_top)
            print('현재 스택 --> ', stack)

        elif select == 'X' or select == 'x':
            print('최종 스택 --> ', stack)
            print('프로그램이 종료됩니다.')
            break

        else:
            print('잘못된 입력입니다. \n 1~4를 입력해주세요.')

