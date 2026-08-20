class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left= Node(20)
root.left.right= Node(25)
root.right.left= Node(30)
root.right.right= Node(35)

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)