splitSTR = 'my name is michael'
splitSTR = splitSTR.split(' ')
array = [0,1,2,3,4,5,6,7,8,9,10]


print(len(splitSTR))
print(splitSTR[3])
print(array[5])

array.append(11)

# same
# del (array[0])
array.remove(0)

print(array)

