## function
class Node():
    def __init__(self):
        self.data = None
        self.link = None



def print_nodes(start):
    current = start
    if current == None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insert_nodes(finddata,insertdata):
    global memory,head,current,pre

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
## value
memory = []
head,current,pre = None,None,None
dataArray = ['민창','희진','용수','서영','현우']

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

    print_nodes(head)

    insert_nodes('민창','화사')
    print_nodes(head)

    insert_nodes('서영','솔라')
    print_nodes(head)

    insert_nodes('지현','문별')
    print_nodes(head)