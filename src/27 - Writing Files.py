# write
with open('fileTest.txt', "a") as writeFile:
    writeFile.write("write test \n")
    writeFile.write("write test 2")

# amend
# with open('fileTest.txt', "a") as writeFile:
#     writeFile.write("write test \n")
#     writeFile.write("write test 2")


openFile = open('fileTest.txt')
print(list(line for line in openFile))
