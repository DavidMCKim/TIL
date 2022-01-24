## 클래스라는 문법을 사용하여 Node() 데이터형 정의
# 클래스 공부 필요!!
class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '민창'

node2 = Node()
node2.data = '희진'
node1.link = node2

node3 = Node()
node3.data = '용수'
node2.link = node3

node4 = Node()
node4.data = '서영'
node3.link = node4

node5 = Node()
node5.data = '현우'
node4.link = node5

# print(node1.data,end=' ')
# print(node1.link.data,end=' ')
# print(node1.link.link.data,end=' ')
# print(node1.link.link.link.data,end=' ')
# print(node1.link.link.link.link.data,end=' ')


## 삽입
newNode = Node()
newNode.data = '지현'
node2.link = newNode
newNode.link = node3
# print(node1.data,end=' ')
# print(node1.link.data,end=' ')
# print(node1.link.link.data,end=' ')
# print(node1.link.link.link.data,end=' ')
# print(node1.link.link.link.link.data,end=' ')
# print(node1.link.link.link.link.link.data,end=' ')

## 삭제
node2.link = node3
del(newNode)
print(node1.data,end=' ')
print(node1.link.data,end=' ')
print(node1.link.link.data,end=' ')
print(node1.link.link.link.data,end=' ')
print(node1.link.link.link.link.data,end=' ')