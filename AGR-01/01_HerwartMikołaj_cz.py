import string

class Vertex:
    def __init__(self, id):
        self.id = id
        self.name = string.ascii_uppercase[id]
        self.degree = 0
        self.neighbours = []
    
    def addNeighbour(self, id):
        if id not in self.neighbours:
            self.neighbours.append(id)
            self.degree+=1


class Graph:
    def __init__(self, fileName):
        self.fileName = fileName
        self.tab = []
        with open (self.fileName, 'r') as file:
            for i in file:
                tab = []
                for j in i:
                    if j == '0' or j == '1':
                        tab.append(int(j))
                self.tab.append(tab)
        #print(self.tab)
        self.vertices = []
        for x in range(0, len(self.tab[0])):
            self.vertices.append(Vertex(x))
        for i in range(0,len(self.tab)):
            for j in range(0, len(self.tab[i])):
                if self.tab[i][j] == 1:
                    self.vertices[i].addNeighbour(j)
        self.edges = []
        for v in self.vertices:
            for e in v.neighbours:
                a = v.id
                b = e
                if a > b:
                    c = a
                    a = b
                    b = c
                if not((a, b) in self.edges):
                    self.edges.append((a,b))
        self.incident = [[0 for col in range(len(self.edges))] for row in range(len(self.vertices))]
        for i in range(0, len(self.edges)):
            e = self.edges[i]
            self.incident[e[0]][i]+=1
            self.incident[e[1]][i]+=1

    
    def tupleIdToName(self, t):
        return (self.vertices[t[0]].name, self.vertices[t[1]].name)

    def printIncidentMatrix(self):
        print("Macierz incydencji: ")
        for i in self.incident:
            print(i)
    
    def printEdgesNames(self):
        print("Krawędzie w grafie: ")
        for i in self.edges:
            print(self.tupleIdToName(i))
    
    def printVerticesDegrees(self):
        print("Stopnie wierzchołków:")
        for i in self.vertices:
            print("* " + i.name + ": " + str(i.degree))

    def neighboursIdToName(self, v):
        tab = []
        for x in v.neighbours:
            tab.append(self.vertices[x].name)
        return tab

    def printMaxVertexDegreeNeighbours(self):
        v = None
        for i in self.vertices:
            if v is None or i.degree > v.degree:
                v = i
        print("Wierzchołek o największym stopniu (" + str(v.degree) + ") to " + v.name + " z somsiadami:")
        print(self.neighboursIdToName(v))

    def printAllNeighbours(self):
        print("Lista następników: ")
        for i in self.vertices:
            print(i.name, self.neighboursIdToName(i))
        


plik = input("Podaj nazwę pliku: ")
graf = Graph(plik)
graf.printVerticesDegrees()
graf.printMaxVertexDegreeNeighbours()
graf.printEdgesNames()
graf.printIncidentMatrix()
graf.printAllNeighbours()