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
    def printConsistentComponents(self):
        n = len(self.vertices)
        C = [0] * n
        cn = 0
        S = []
        vOrder = []
        skladowe = []
        print(str(n))
        for i in range(n):
            if C[i] > 0:
                continue
            cn+=1
            skladowe.append([])
            S.append(i)
            skladowe[cn-1].append(i)
            vOrder.append(i)
            C[i] = cn
            vx = S[-1]
            while len(S):
                v = self.vertices[vx]
                vN = len(v.neighbours)
                vV = 0
                for x in v.neighbours:
                    if C[x] > 0:
                        vV+=1
                if vN == vV:
                    S.pop()
                    if len(S) == 0:
                        break
                    vx = S[-1]
                    continue
                for u in v.neighbours:
                    if C[u] > 0:
                        continue
                    else:
                        S.append(u)
                        vx = S[-1]
                        skladowe[cn-1].append(u)
                        vOrder.append(u)
                        C[u] = cn
                        break
        print(vOrder)
        print("Spójne składowe: " + str(cn))
        for i in range(1,cn+1):
            print("*składowa: " + str(i))
            print(skladowe[i-1])



plik = input("Podaj nazwę pliku: ")
graf = Graph(plik)
graf.printConsistentComponents()