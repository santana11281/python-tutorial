def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while array[j] > temp and j>-1:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = temp
    return array


myArr = [6, 5, 4, 3, 2, 1, 0]
insertionSort(myArr)
print(myArr)
