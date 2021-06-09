class Graphadj():
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.graphadj = [[[] for j in range(nvertices)] for i in range(nvertices)]
    
    def print_graph(self):
        print(self.graphadj)

    #Adicionar vértices e arestas
    def add_aresta(self, a, b, dist):
        if a > self.nvertices or b > self.nvertices:
            print("indices fora do escopo")
            return
        self.graphadj[a][b].append(b)
        self.graphadj[a][b].append(dist)

    def add_vertice(self):
        self.nvertices += 1
        for vet in self.graphadj:
            vet.append([])
        self.graphadj.append([[] for i in range(self.nvertices)])
    
    #Calcular o grau de um dado vértice
    def grau(self, v):
        g = 0
        for i in range(self.nvertices):
            if len(self.graphadj[i][v]) != 0:
                g += 1
            if v == i:
                for j in range(self.nvertices):
                    if len(self.graphadj[i][j]) != 0:
                        g += 1
        return g

    #Responder se um vértice é alcançável diretamente a partir de outro    
    def alcancavel_diretamente(self, a, b):
        if len(self.graphadj[a][b]) != 0:
            return True
        else:
            return False

    #Responder se um vértice é alcançável a partir de outro
    def alcancavel(self, a, b ):
        if self.alcancavel_diretamente(a, b):
            return True
        else:
            for i in range(self.nvertices):
                if self.alcancavel_diretamente(a, i):
                    if self.alcancavel(i, b):
                        return True
            return False

print("Qual o número de vértices?")
n = int(input())
g = Graphadj(n)
while(True):
    print("1 - Adicionar arestas")
    print("2 - Printar grafo")
    print("3 - Adicionar Vertice")
    print("4 - Calcular grau do vertice")
    print("5 - Verificar se vetice é diretamente alcançável")
    print("6 - Vértice é alcançável a partir de outro")
    print("0 - Sair")
    op = int(input())
    if op == 0:
        break
    elif op == 1:
        print("a -> b")
        print("a:")
        a = int(input())
        print("b: ")
        b = int(input())
        print("dist: ")
        dist = int(input())
        g.add_aresta(a, b, dist)
    elif op == 2:
        g.print_graph()
    elif op == 3: 
        g.add_vertice()
    elif op == 4:
        print("digite um vertice: ")
        v = int(input())
        print("o Grau do vertice %i é: %i"%(v, g.grau(v)))
    elif op == 5:
        print("a -> b")
        print("a:")
        a = int(input())
        print("b:")
        b = int(input())
        if g.alcancavel_diretamente(a,b):
            print("Diretamente alcançavel")
        else:
            print("Não é diretamente alcançavel")
    elif op == 6:
        print("a -> b")
        print("a:")
        a = int(input())
        print("b:")
        b = int(input())
        if g.alcancavel(a,b):
            print("Alcançavel")
        else:
            print("Não é alcançavel")
    else:
        print("Opção invalida")
