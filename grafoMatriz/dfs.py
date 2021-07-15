from stack import Stack
from graph import Graph
class Dfs:
    def __init__(self, g, v):
        self.g = g
        self.v = v
        pass

    def graphDfs(self):
        nun = []
        for i in range(self.g.N):
            nun.append(-1)
        nun[self.v] = 0

        p = Stack()
        p.put(self.v)
        
        count = 1
        while(p.tam() != 0):
            v = p.get()
            if(nun[v] == -1):
                nun[v] = count
                count += 1
            for i in range(g.tam()):
                if(self.g.adjacente(v, i)):
                    p.put(i)
        return nun

""" g = Graph(6)
g.graph =  [[0,0,0,0,1,1], [1,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,1,1,0,0], [0,0,0,0,0,0]]
dfs = Dfs(g, 0)
print(dfs.graphDfs()) """