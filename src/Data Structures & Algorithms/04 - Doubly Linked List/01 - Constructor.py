class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev =None
        self.length -= 1
        return temp.value


def printList(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


myDoublyLinkedList = DoublyLinkedList(7)
# myDoublyLinkedList.append(8)
# myDoublyLinkedList.append(9)
# myDoublyLinkedList.pop()
print(myDoublyLinkedList.pop())
# printList(myDoublyLinkedList)
