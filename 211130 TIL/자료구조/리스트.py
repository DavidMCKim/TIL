## functions(함수)
# add(추가)
def addData(name):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = name

# insert(삽입)
def insertData(position,name):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1,position,-1):
        katok[i] = katok[i-1]
    katok[position] = name

# delete(삭제)
def delData(position):
    klen = len(katok)
    katok[position] = None
    for i in range(position,klen-1):
        katok[i] = katok[i+1]
        ## katok[i+1] = None ## 생략가능
    del katok[klen-1]

## vari(변수)
katok = ['안기용','김민창','조소진','이새봄','여정문']
select = -1 # 1 : add, 2 : insert, 3 : delete, 4 : end

## main
if __name__ == '__main__':
    print(katok)
    while select != 4:
        select =int(input('숫자를 입력하세요 : '))
        if select == 1:
            name = input('삽입할 데이터를 입력하세요 : ')
            addData(name)
            print(katok)
        elif select == 2:
            position = int(input('삽입할 위치를 입력하세요 : '))
            name = input('삽입할 데이터를 입력하세요 : ')
            insertData(position,name)
            print(katok)
        elif select == 3:
            position = int(input('삭제할 위치를 입력하세요 : '))
            delData(position)
            print(katok)
        elif select == 4:
            print(katok)
            pass
        else:
            print('1~4를 입력하세요')
    print(katok)

