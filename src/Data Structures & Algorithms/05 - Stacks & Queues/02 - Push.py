class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def printList(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1


myStack = Stack(4)
myStack.push(5)
myStack.push(6)

myStack.printList()
