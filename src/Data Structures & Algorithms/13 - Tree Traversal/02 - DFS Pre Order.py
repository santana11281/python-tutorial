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

    def DFSPreOrder(self):
        results = []

        def traverse(currentNode):
            results.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return results


myBinaryTree = BinaryTree()
myBinaryTree.insert(47)
myBinaryTree.insert(21)
myBinaryTree.insert(76)
myBinaryTree.insert(18)
myBinaryTree.insert(27)
myBinaryTree.insert(52)
myBinaryTree.insert(82)

print(myBinaryTree.DFSPreOrder())

# [47, 21, 18, 27, 76, 52, 82]
