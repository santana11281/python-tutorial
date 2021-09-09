def InsertionSort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1
        while temp < myList[j] and j > -1:
            myList[j + 1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList


def mySort(arr):
    newArr = []
    min2 = 0

    for i in arr:
        min = i
        for j in arr:
            print(f"comparing {i} with {j}    or     {i}****{j}")
            if i < j:
                min = i
            else:
                min = j

        print(min,"*")
        # print("done min was -> ", min)

    # print(newArr, "<-newArr")
    return newArr


arr = [1, 3, 2, 8, 5, 6, 7, 4]
mySort(arr)
# print(mySort(arr))

# print(InsertionSort([1, 2, 4, 3, 5, 6]))
