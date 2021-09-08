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
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        temp = self.root
        while temp is not None:
            if newNode.value == temp.value:
                return False
            elif newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                else:
                    temp = temp.left
            elif newNode.value > temp.value:
                if temp.right is None:
                    temp.right = newNode
                else:
                    temp = temp.right
                    return True
            return False


myBinaryTree = BinaryTree()
myBinaryTree.insert(2)
myBinaryTree.insert(1)
myBinaryTree.insert(3)

print(myBinaryTree.root.value)
print(myBinaryTree.root.left.value)
print(myBinaryTree.root.right.value)

# parse = json.dumps(myBinaryTree.__dict__)
# print(parse)
