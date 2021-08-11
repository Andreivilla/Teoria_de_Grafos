from graph import Graph
class Prim:
    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.k = [float('inf') for i in range(self.g.N)]
        self.p = [None for i in range(self.g.N)]
        self.q = [() for i in range(self.g.N)]


    def agm(self):


        self.k[self.s] = 0
        
        for i in range(self.g.N):
            self.q.append((i, self.k[i]))
        
        while(len(self.q) != 0):
            #print("-------------------")
            #print(f'P {self.p}')
            #print(f'K {self.k}')
            #print(f'Q {self.q}')
            #print("-------------------")

            u = self.minQ(self.q)                
            self.q.remove(u)
            for v in range(self.g.N):
                if self.g.adjacente(u[0], v):
                    if self.verificaVQ(v, self.q) and self.g.peso(u[0], v) < self.k[v]:
                        self.p[v] = u[0]
                        self.k[v] = self.g.peso(u[0], v)
        return self.k

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
        for i in self.q:
            if i[0] = 




g = Graph(5)
g.graph =  [[0, 20, 10, 0, 0], [20, 0, 5, 20, 5], [10, 5, 0, 0, 15], [0, 20, 0, 0, 10], [0, 5, 15, 10, 0]]
prim = Prim(g, 0)
print(prim.agm())