from graph import Graph
from dfs import Dfs

class Hamiltoniano:
    def __init__(self, g):
        self.g = g

    def verifCiclo(self, v = 0):
        dfs = Dfs(self.g, v)
        listaDfs = dfs.GRAPHdfs()
        if(g.adjacente(listaDfs[len(listaDfs)-1], v)):
            return True
        else:
            if(v < g.N):
                return self.verifCiclo(v+1)
            else:
                return False

""" g = Graph(5)
g.graph =  [[0, 1, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 1, 0, 1, 0]] """
g = Graph(6)
g.graph = [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]

h = Hamiltoniano(g)
print(h.verifCiclo())