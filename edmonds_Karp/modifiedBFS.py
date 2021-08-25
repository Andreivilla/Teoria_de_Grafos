from _typeshed import Self
from graph import Graph
from queue import Queue

class ModifiedBFS:
    def __init__(self, g, s, t, parent):
        self.g = g
        self.s = s#s é um vertice qualquer
        self.t = t
        self.parent = parent
        self.inexplorados = [i for i in range(self.g.N)]

    def bfs(self):
        q = Queue()
        q.put(self.s)
        self.inexplorados.remove(self.s)

        while q.tam() > 0:
            u = q.get()
            for w in range(self.g.N):
                if g.adjacente(u, w) and w in self.inexplorados:
                    q.get(w)
                    self.inexplorados.remove(w)
                    self.parent[w] = u
                    if w == self.t:
                        return True
        return False

