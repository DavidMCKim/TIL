## functions
def addData(data):
    test.append(None)
    length = len(test)
    test[length-1] = data
    print(test)

def insertData(position,data):
    test.append(data)
    length = len(test)
    for i in range(length-1,position,-1):
        test[i] = test[i-1]
        test[i-1] = None
    test[position] = data
    print(test)

def delData(position):
    length = len(test)
    for i in range(position,length-1):
        test[i] = test[i+1]
        test[i+1] = None
    del test[length-1]
    print(test)

## vari
test = []
select = -1

## main
if __name__ == '__main__':
    print(test)
    while select != 4:
        select = int(input('원하는 숫자를 입력하세요 (1:add / 2:insert / 3:delete / 4:exit): '))
        if select == 1:
            data = input('추가하고자 하는 데이터를 입력하세요 : ')
            addData(data)

        elif select == 2:
            position = int(input('삽입하고자하는 위치를 입력하세요 : '))
            data = input('추가하고자 하는 데이터를 입력하세요 : ')
            insertData(position,data)

        elif select == 3:
            position = int(input('삭제하고자하는 위치를 입력하세요 : '))
            delData(position)

        elif select == 4:
            print(f'test : {test}')
            print('끝!!')
            break

        else:
            print('잘못된 입력입니다.\n1~4 숫자를 입력하세요~^^')
