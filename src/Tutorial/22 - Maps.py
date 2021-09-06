from random import shuffle

fruits = ['avocado', 'banana', 'grape']
anagram = []


def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ' '.join(anagram)

def printWord(words):
    for word in words:
        return word



# print( jumble(fruits).split(' '))
# printWord(fruits)
print(list(map(printWord,fruits)))
