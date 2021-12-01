## function
def addData(data):
    kakao.append(None)
    klen = len(kakao)
    kakao[klen-1] = data
    print(kakao)

def insertData(position,data):
    kakao.append(None)
    klen = len(kakao)
    for i in range(klen-1,position,-1):
        kakao[i] = kakao[i-1]
    kakao[position] = data
    print(kakao)

def deleteData(position):
    klen = len(kakao)
    for i in range(position,klen-1):
        kakao[i] = kakao[i+1]
        kakao[i+1] = None
    del kakao[klen-1]

## vari
kakao = []
select = -1

## main
if __name__ == '__main__':
    print('원래 리스트 : ',kakao)
    while select != 4:
        select =int(input('숫자를 입력하세요 : '))
        if select == 1:
            name = input('삽입할 데이터를 입력하세요 : ')
            addData(name)
            print(f'{name}이 추가된 리스트 : {kakao}')
        elif select == 2:
            position = int(input('삽입할 위치를 입력하세요 : '))
            name = input('삽입할 데이터를 입력하세요 : ')
            insertData(position,name)
            print(f'{position}위치에 {name}이 삽입된 리스트 : {kakao}')
        elif select == 3:
            position = int(input('삭제할 위치를 입력하세요 : '))
            deleteData(position)
            print(f'{position}위치 데이터가 삭제된 리스트 : {kakao}')
        elif select == 4:
            print(kakao)
            pass
        else:
            print('1~4를 입력하세요')
    print(kakao)