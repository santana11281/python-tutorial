import json


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


myBinaryTree = BinaryTree()
myBinaryTree.insert(2)
myBinaryTree.insert(1)
myBinaryTree.insert(3)

print(myBinaryTree.root.value)
print(myBinaryTree.root.left.value)
print(myBinaryTree.root.right.value)

# parse = json.dumps(myBinaryTree.__dict__)
# print(parse)
