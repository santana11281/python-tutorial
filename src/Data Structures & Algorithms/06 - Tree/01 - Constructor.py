import json


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





class BinaryTree:
    def __init__(self):
        self.root = None




myBinaryTree = BinaryTree()

parse = json.dumps(myBinaryTree.__dict__)
print(parse)
