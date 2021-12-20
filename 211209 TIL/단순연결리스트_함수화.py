## functions
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current = current.link
        print(current.data,end=' ')
    print()

def insertNode(finddata,insertdata):
    global current, head, pre

    if head.data == finddata:
        node = Node()
        node.data = insertdata
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link

        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertdata
    current.link = node

def deleteNode(finddata):
    global current, head, pre

    if head.data == finddata:
        current = head
        head = current.link
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == finddata:
            pre.link = current.link
            del current
            return

## vari
memory = []
current, head, pre = None, None, None
dataArray = ['정문','기용','새봄','민창','소진']
select = -1

## main
if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

while select != 3:
    select = int(input('숫자를 입력하세요(1~3) : '))

    if select == 1:
        finddata = input('찾을 데이터를 입력하세요 : ')
        insertdata = input('삽입할 데이터를 입력하세요 : ')
        insertNode(finddata,insertdata)
        printNodes(head)

    elif select == 2:
        finddata = input('삭제할 데이터를 입력하세요 : ')
        deleteNode(finddata)
        printNodes(head)

    elif select == 3:
        print('끝~!!')
        break

    else:
        print('잘못된 입력입니다~^^')
        print('1~3을 입력해주세요.')

    # printNodes(head)
    #
    # insertNode('기용','윈터')
    # printNodes(head)
    #
    # insertNode('봉봉','민정')
    # printNodes(head)
    #
    # deleteNode('윈터')
    # printNodes(head)
    #
    # deleteNode('민정')
    # printNodes(head)