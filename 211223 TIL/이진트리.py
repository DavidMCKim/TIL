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

print(node1.data, end=' ')
print()
print(node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end=' ')
