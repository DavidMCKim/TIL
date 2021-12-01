class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = 'naver-crawling'

node2 = Node()
node2.data = 'hadoop'
node1.link = node2

node3 = Node()
node3.data = 'spark'
node2.link = node3

node4 = Node()
node4.data = 'MySQL'
node3.link = node4

node5 = Node()
node5.data = 'AWS'
node4.link = node5

print('************************ 단순 연결 리스트  ************************')

print(node1.data, end = ' ')
print(node1.link.data, end = ' ')
print(node1.link.link.data, end = ' ')
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data)

print('\n************************ 노드 추가  ************************')

newnode = Node()
newnode.data = 'Django'
newnode.link = node5
node4.link = newnode

print(node1.data, end = ' ')
print(node1.link.data, end = ' ')
print(node1.link.link.data, end = ' ')
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data, end = ' ')
print(node1.link.link.link.link.link.data)

print('\n************************ 노드 추가  ************************')

temp = Node()
temp.data = '김민창'
temp.link = newnode
node4.link = temp

print(node1.data, end = ' ')
print(node1.link.data, end = ' ')
print(node1.link.link.data, end = ' ')
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data, end = ' ')
print(node1.link.link.link.link.link.data, end = ' ')
print(node1.link.link.link.link.link.link.data)

print('\n************************ 삭제 후  ************************')

# node4.link = newnode를 해도 되는데 temp.link로 하는 이유는?
# 여러개의 노드가 있을 때 어느 위치를 정확히 모르니 그 다음 노드의 link를 거는건감??

node4.link = temp.link
del(temp)

print(node1.data, end = ' ')
print(node1.link.data, end = ' ')
print(node1.link.link.data, end = ' ')
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data, end = ' ')
print(node1.link.link.link.link.link.data)