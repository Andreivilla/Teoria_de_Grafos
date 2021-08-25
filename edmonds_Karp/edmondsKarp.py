from _typeshed import Self
from graph import Graph
from modifiedBFS import ModifiedBFS

class EdmondsKarp:
    def __init__(self, g, source, sink):
        self.g = g
        self.source = source
        self.sink = sink

    def ek(self):
        parent = []
        max_flow = 0
        mbfs = ModifiedBFS(self.source, self.sink, parent)
        while mbfs.bfs():
            path_flow = float('inf')
            s = self.sink
            while s != self.source:
                path_flow = min(path_flow, self.g.peso(s, parent[s]))
            max_flow += path_flow
            v = self.sink
            while v != self.source:
                u = parent[v]