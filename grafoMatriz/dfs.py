from graph import Graph

class Dfs:
    def __init__(self, g, v):
        self.g = g
        self.v = v
        self.pre = []
        self.cnt = 0

    def GRAPHdfs(self):
        for i in range(self.g.N):
            self.pre.append(-1)

        for i in range(self.g.N):
            if self.pre[i] == -1:
                self.dfsR(i)
        return self.pre

    def dfsR(self, v):
        self.pre[v] = self.cnt
        self.cnt += 1
        for i in range(self.g.N):
            if self.g.adjacente(v, i):
                if self.pre[i] == -1:
                    self.dfsR(i)

""" g = Graph(5)
g.graph =  [[0,1,0,0,1,0,0], [0,0,0,0,0,0,0], [1,0,0,1,1,0,0], [0,0,0,0,0,1,1], [0,1,0,0,0,0,1], [0,1,0,0,0,0,0]]
dfs = Dfs(g, 0)
print(dfs.GRAPHdfs()) """