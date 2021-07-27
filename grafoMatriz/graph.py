class Graph():
    def __init__(self, nvertices):
        self.N = nvertices
        self.graph = [[0 for column in range(nvertices)]
        for row in range(nvertices)]
        self.V = ['0' for column in range(nvertices)]

    def nameVertex(self):
        for i in range(self.N):
            print("Qual o rotúlo do vértice %i?"%(i))
            self.V[i]=input()
            

    def setEdge(self,u,v,w):
        self.graph[u][v]=w
    
    def loadEdges(self):
        for i in range(self.N):
            for j in range(self.N):
                if i!=j:
                    print("Qual o peso entre %c e %c?"%(self.V[i],self.V[j]))
                    self.setEdge(i,j,input())

    def adjacente(self, a, b):
        try:
            if(self.graph[a][b] != 0):
                return True
            else:
                return False
        except:
            return False
    
    def tam(self):
        return self.N

    def peso(self, a, b):
        return self.graph[a][b]

    def grau(self, a):
        count =0
        for i in range(self.N):
            if self.g[0][i] != 0:
                count += 1
        return count