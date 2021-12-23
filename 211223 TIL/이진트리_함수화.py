def preorder(node): # 전위 순회
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

def inorder(node): # 중위 순회
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

def postorder(node): # 후위 순회
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = '민창'

node2 = TreeNode()
node2.data = '새봄'
node1.left = node2

node3 = TreeNode()
node3.data = '소진'
node1.right = node3

node4 = TreeNode()
node4.data = '기용'
node2.left = node4

node5 = TreeNode()
node5.data = '정문'
node2.right = node5

node6 = TreeNode()
node6.data = '용수'
node3.left = node6

print('전위 순회 : ', end=' ')
preorder(node1)
print('끝')

print('중위 순회 : ', end=' ')
inorder(node1)
print('끝')

print('후위 순회 : ', end=' ')
postorder(node1)
print('끝')