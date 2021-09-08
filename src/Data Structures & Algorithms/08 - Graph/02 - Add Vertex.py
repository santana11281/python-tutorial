class Grapth:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, " : ", self.adj_list[vertex])


myGraph = Grapth()

myGraph.addVertex("A")
myGraph.addVertex("B")
myGraph.addVertex("C")
myGraph.addVertex("D")
myGraph.addEdge("A","D")
myGraph.addEdge("A","B")
myGraph.printGraph()
