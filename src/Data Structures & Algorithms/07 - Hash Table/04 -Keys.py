class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def getItem(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]

    def printTable(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)


myHashTable = HashTable()

myHashTable.set_item("Michael", 23)
myHashTable.set_item("Ambar", 13)
myHashTable.set_item("Mauricio", 7)
myHashTable.set_item("Mauricio", 7)

print(myHashTable.getItem("Ambar"))

# myHashTable.printTable()
