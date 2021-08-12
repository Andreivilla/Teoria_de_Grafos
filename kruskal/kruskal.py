from graph import Graph


class Kruskal:
    def __init__(self, g, v):
        self.g = g
        self.s = [[i] for i in range(self.g.N)]
        self.a = []
        self.e = []

    def amg(self):
        self.geraE()
        self.ordenaE()

        for e in self.e:# e = (u,v,custo)
            if self.s[e[0]] != self.s[e[1]]:
                self.a.append((e[0], e[1]))
                x = self.s[e[0]] + self.s[e[1]]
                for y in x:
                    self.s[y] = x
        return self.a

    def geraE(self):
        lstVisitados = []
        for i in range(self.g.N):
            for j in range(self.g.N):
                if self.g.graph[i][j] != 0 and (j,i) not in lstVisitados:
                    self.e.append((i,j,self.g.graph[i][j]))
                    lstVisitados.append((i,j))
    
    def ordenaE(self):
        for i in range(len(self.e)):
            for j in range(i+1,len(self.e)):
                if self.e[i][2] > self.e[j][2]:
                    aux = self.e[i]
                    self.e[i] = self.e[j]
                    self.e[j] = aux

g = Graph(5)
g.graph = [[0, 15, 12, 0, 0], [15, 0, 6, 13, 5], [12, 6, 0, 6, 0], [0, 13, 6, 0, 0], [0, 5, 0, 0, 0]]
kruskal = Kruskal(g, 0)
print(f'O caminho que irá diminuir o impacto ambiental é dado por {kruskal.amg()}')