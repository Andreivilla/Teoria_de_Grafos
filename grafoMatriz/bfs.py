'''enquanto a fila não estiver vazia
    retire um vértice v da fila
    para cada vizinho w de v
        se w não está numerado
            então numere w
                ponha w na fila'''

from queue import Queue
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

""" g = Graph(6)
g.graph =  [[0,0,1,1,1,0], [0,1,0,0,1,0], [0,0,0,0,1,0], [0,0,0,0,1,1], [0,0,0,0,0,1], [0,1,0,0,0,0]]
bfs = Bfs(g, 0)
print(bfs.graphBfs())

g1 = Graph(6)
g1.graph =  [[0,1,1,0,0,1], [1,0,1,0,0,0], [1,1,0,1,1,0], [0,0,1,0,1,1], [0,0,1,1,0,0], [1,0,0,1,0,0]]
bfs1 = Bfs(g1, 0)
print(bfs1.graphBfs()) """