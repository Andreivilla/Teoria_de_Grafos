from graph import Graph
class Prim:
    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.k = [float('inf') for i in range(self.g.N)]
        self.p = [-1 for i in range(self.g.N)]
        self.q = [(i, self.k[i]) for i in range(self.g.N)]

    def agm(self):
        self.p[self.s] = 0
        self.k[self.s] = 0
        
        for i in range(self.g.N):
            self.q[i] = (i, self.k[i])

        while(len(self.q) != 0):
            self.atualizaQ()

            print("-------------------")
            print(f'P {self.p}')
            print(f'K {self.k}')
            print(f'Q {self.q}')
            print("-------------------")

            u = self.minQ(self.q)                
            self.q.remove(u)
            for v in range(self.g.N):
                if self.g.adjacente(u[0], v):
                    if self.verificaVQ(v, self.q) and self.g.peso(u[0], v) < self.k[v]:
                        self.p[v] = u[0]
                        self.k[v] = self.g.peso(u[0], v)

    def verificaVQ(self, v, q):
        for i in q:
            if i[0] == v:
                return True
        return False
    
    def minQ(self, q):
        minK = q[0][1]
        minTupla = q[0]
        for i in q:
            if i[1] < minK:
                minTupla = i
                minK = i[1]
        return minTupla

    def atualizaQ(self):
        for i in range(len(self.q)):
            lst = list(self.q[i])
            lst[1] = self.k[self.q[i][0]]
            self.q[i] = tuple(lst)
                

g = Graph(5)
g.graph = [[0, 15, 12, 0, 0], [15, 0, 6, 13, 5], [12, 6, 0, 6, 0], [0, 13, 6, 0, 0], [0, 5, 0, 0, 0]]
prim = Prim(g,0)
prim.agm()
print(prim.p)