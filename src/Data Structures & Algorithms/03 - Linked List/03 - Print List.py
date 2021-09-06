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

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        return True

    def pop(self):
        temp = self.head
        if self.length == 0:
            return None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
                if temp.next is None:
                    pre.next = None
                    # temp = None


def printList(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


myLinkList = LinkedList(23)
myLinkList.append(24)
myLinkList.append(25)
myLinkList.append(26)
myLinkList.pop()
printList(myLinkList)
