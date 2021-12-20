class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '기용'

node2 = Node()
node2.data = '정문'
node1.link = node2

node3 = Node()
node3.data = '민창'
node2.link = node3

# print(node1.link.link.data)

newnode = Node()
newnode.data = '윈터'
node1.link = newnode
newnode.link = node2

# print(node1.link.link.data)

# current = node1
# print(current.data, end=' ')
# while current.link != None:
#     current = current.link
#     print(current.data, end=' ')

node1.link = node2
del(newnode)

current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')