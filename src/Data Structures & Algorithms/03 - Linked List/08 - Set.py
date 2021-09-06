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

        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self.head

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def setValue(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False





    # def ifContains(self, value):
    #     currentNode = self.head
    #     while currentNode is not None:
    #         currentNode = currentNode.next
    #         print(currentNode.value)
    #         if currentNode.value == value:
    #             return True
    #         else:
    #             return False



def printList(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


myLinkList = LinkedList(23)
myLinkList.append(24)
myLinkList.append(25)
myLinkList.prepend(22)
myLinkList.setValue(0,1)
# print(myLinkList.get(0))
printList(myLinkList)
