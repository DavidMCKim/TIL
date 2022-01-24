# function - 선형리스트 생성코드 함수화
def add_list(data):
    katok_list.append(None)
    length = len(katok_list)
    katok_list[lenght - 1] = data
    print(katok_list)


def insert_list(position,data):
    katok_list.append(None)
    length = len(katok_list)

    for i in range(length-1,position,-1):
        katok_list[i] = katok_list[i-1]
        katok_list[i-1] = None
    katok_list[position] = data
    print(katok_list)


def delete_list(position):
    length = len(katok_list)
    for i in range(position,length-1):
        katok_list[i] = katok_list[i+1]
        katok_list[i+1] = None
    del katok_list[-1]
    print(katok_list)

# value
katok_list = []
lenght = len(katok_list)
select = -1
# main
if __name__ == '__main__':
    while select != 4:
        select = int(input('번호 선택(1:추가, 2:삽입, 3:삭제, 4:종료) : '))
        if select == 1:
            data = input()
            add_list(data)

        elif select == 2:
            position = int(input())
            data = input()
            insert_list(position,data)

        elif select == 3:
            position = int(input())
            delete_list(position)

        elif select == 4:
            print('프로그램이 종료되었습니다.')
            print('리스트\n',katok_list)