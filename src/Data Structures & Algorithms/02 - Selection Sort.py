def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
def selectionSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i,len(array)):
            if array[j] < array[min]:
                min = j
        swap(array, min, i)
    return array


myArr = [6, 5, 4, 3, 2, 1, 0]
selectionSort(myArr)

print(myArr)
