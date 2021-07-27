""" from queue import Queue
from graph import Graph
class Bfs:
    def __init__(self, g, v ):
        self.g = g
        self.v = v
        pass

    def graphBfs(self):
        fila = Queue()
        fila.put(self.v)
        nun = []
        nun.append(0)
        for i in range(self.g.N-1):
            nun.append(-1)
        
        count = 1
        while(fila.tam() != 0):
            v = fila.get()
            for i in range(self.v,g.tam()):
                if(self.g.adjacente(v, i)):
                    if(nun[i] == -1):
                        nun[i] = count
                        count += 1
                        fila.put(i)
        return nun

g = Graph(6)
g.graph =  [[0,0,1,1,1,0], [0,1,0,0,1,0], [0,0,0,0,1,0], [0,0,0,0,1,1], [0,0,0,0,0,1], [0,1,0,0,0,0]]
bfs = Bfs(g, 0)
print(bfs.graphBfs()) """

from queue import Queue
from graph import Graph
class Bfs:
    def __init__(self, g, v ):
        self.g = g
        self.v = v
        self.num = []

    def GRAPHbfs(self):
        cnt = 0
        for i in range(self.g.N):
            self.num.append(-1)
        queue = Queue()
        self.num[self.v] = cnt
        queue.put(self.v)

        while queue.tam() != 0:
            v = queue.get()
            for i in range(self.g.N):
                if self.g.adjacente(v, i):
                    if self.num[i] == -1: 
                        cnt += 1
                        self.num[i] = cnt
                        queue.put(i)
        return self.num


g = Graph(6)
g.graph = [[0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0]]
bfs = Bfs(g, 0)
print(bfs.GRAPHbfs())