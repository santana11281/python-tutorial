def swap(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp


def pivot(myList, pivotIndex, endIndex):
    swapIndex = pivotIndex

    for i in range(pivotIndex + 1, endIndex + 1):
        if myList[i] < myList[pivotIndex]:
            swapIndex += 1
            swap(myList, swapIndex, i)
    swap(myList, pivotIndex, swapIndex)
    return swapIndex


def QuickSort_helper(myList, left, right):
    if left < right:
        pivotIndex = pivot(myList, left, right)
        QuickSort_helper(myList, left, pivotIndex - 1)
        QuickSort_helper(myList, pivotIndex + 1, right)
    return myList


def quickSort(myList):
    return QuickSort_helper(myList, 0, len(myList) - 1)


myList = [7, 6, 1,4 , 3, 2, 5]

print(quickSort(myList))

# print(myList)
