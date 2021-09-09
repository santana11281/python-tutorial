def selectionSort(myList):
    for i in range(len(myList) - 1):
        minIndex = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[minIndex]:
                minIndex = j
        if i != minIndex:
            temp = myList[i]
            myList[i] = myList[minIndex]
            myList[minIndex] = temp
    return myList


print(selectionSort([4, 2, 6, 5, 1, 3]))
