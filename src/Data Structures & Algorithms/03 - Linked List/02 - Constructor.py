import json


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1


myLinkList = LinkedList(23)

jsonStr = json.dumps(myLinkList.__dict__)
print(jsonStr)
# print(myLinkList.head.value)
