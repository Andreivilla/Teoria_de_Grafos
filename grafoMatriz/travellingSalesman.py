from graph import Graph
class TravellingSalesman:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        
    def solve(self):
        for i in range(3, self.g.N):
            for subset in combinations(i, self.g.N):
                if self.s not in  subset: continue
                for 