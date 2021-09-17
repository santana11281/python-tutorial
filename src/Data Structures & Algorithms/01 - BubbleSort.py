def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j + 1] < array[j]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print(array)


newArr = [6, 5, 4, 3, 2, 1, 0]
bubbleSort(newArr)


