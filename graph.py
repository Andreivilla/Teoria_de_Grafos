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

    #1
    def adjacente(self):
        print("Digite 2 vertices: ")
        a = input()
        b = input()

        for i in range(self.N):
            if(self.V[i] == a):
                a = i
            if(self.V[i] == b):
                b = i

        if(self.graph[a][b] != 0 or self.graph[b][a] != 0):
            print("Adjacente")
            print("Distancia entre %c e %c é %c"%(self.V[a],self.V[b],self.graph[a][b]))
            print("Distancia entre %c e %c é %c"%(self.V[a],self.V[b],self.graph[b][a]))
        else:
            print("Não adjacente")
    #2
    def grau(self):
        print("Digite um vetrice")
        g = 0
        v = input()
        for i in range(self.N):
            if(self.V[i] == v):
                v=i
        for i in range(self.N):
            if(self.graph[v][i] != 0):
                g += 1
        print("Grau: %i"%int(g))
    #3
    def subgrafo(self, verif):
        count_iguais = 0
        v1 = 0
        if(verif.N > self.N):
            return False

        for i in range(self.N):
            if(self.V[i] == verif.V[0]):
                v1 = i
                break
            else:
                False
            for i in range(v1+verif.N):
                for j in range(v1+verif.N):
                    if(self.graph[v1+i][v1+j] == self.graph[i][j]):
                        count_iguais += 1
                    else:
                        return False
            return True
    #4
    def arestas(self):
        a = 0
        for i in range(self.N):
            for j in range(self.N): 
                if(self.graph[i][j] != 0):
                    a += 1
        print("Numero de arestas: %i"%(a/2))
    #5
    def completo(self):
        for i in range(self.N):
            contalinha = 0
            for j in range(self.N):
                if(self.graph[i][j] != 0):
                    contalinha += 1
            if(contalinha == 0):
                return False
        return True


    

print("Qual o número de vértices?")
n = int(input())
g = Graph(n)
g.nameVertex()
print("Inserir Arestas: ")
g.loadEdges()

while(True):
    print("1 - Verifica adjacentes")
    print("2 - Verifica grau de um vertice")
    print("3 - Verifica se é subgrafo")
    print("4 - Numero de arestas")
    print("5 - verifica se é um grafo completo")
    print("0 - Sair")
    op = input()
    print(op)
    if(op == '1'):
        
        g.adjacente()
    elif(op == '2'):
        g.grau()
    elif(op == '3'):
        print("Qual o número de vértices?")
        n1 = int(input())
        g1 = Graph(n1)
        g1.nameVertex()
        print("Inserir Arestas: ")
        g1.loadEdges()

        if(g.subgrafo(g1)):
            print("é subgrafo")
        else:
            print("Não é subgrafo")
    elif(op == '4'):
        g.arestas()
    elif(op == '5'):
        if(g.completo()):
            print("Completo")
        else:
            print("Não é completo")
    elif(op == '0'):
        break
    else:
        print("Opicao invalidda")
