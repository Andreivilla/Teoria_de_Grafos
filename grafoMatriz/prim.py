from graph import Graph
class Prim:
    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.k = []
        self.p = []


    def agm(self):
        for i in range(g.N):
            k[i] = float('inf')
            p[i] = float('inf')

        k[self.s] = 0
        