testFile = open('fileTest.txt')


# for line in testFile:
#     print(line.rstrip())


# testFile.seek(0)
# line = testFile.readlines()
# print(line)

#
# testFile.seek(50)
# file_text = testFile.read(100)
# print(file_text)
# testFile.close()

def sequence_filter(line):
    return 'Python' not in line


with open('fileTest.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter,lines)))
