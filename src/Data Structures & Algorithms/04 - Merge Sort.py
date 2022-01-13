import math


def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
    while i < len(array1):
        combined.append(array1[i])
        i += 1
    while j < len(array2):
        combined.append(array2[j])
        j += 1
    return combined







def mergeSort(array3):
    if len(array3) == 1:
        return array3
    mid = math.floor(len(array3) / 2)
    left = array3[:mid]
    right = array3[mid:]
    return merge(mergeSort(left), mergeSort(right))


arr3 = [6, 5, 4, 3, 2, 1, 0]
arr1 = [1, 4, 5, 8]
arr2 = [2, 3, 6, 7]

print(mergeSort(arr3))
# merge(arr1, arr2)
