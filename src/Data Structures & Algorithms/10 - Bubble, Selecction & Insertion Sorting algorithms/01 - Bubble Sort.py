def BubbleSort(myList):
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
    return myList


print(BubbleSort([4, 2, 6, 5, 1, 3]))
