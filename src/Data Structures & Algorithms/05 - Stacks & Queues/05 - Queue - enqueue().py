class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True

    def dequeue(self):
        temp = self.first
        if self.length == 0:
            return None
        else:
            self.first = temp.next
            temp = None

    def printList(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


myQueue = Queue(1)

myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)

myQueue.printList()

