from graph import Graph
class Dijkistra:
    def __init__(self, G, s):
        self.g = G
        self.s = s
        pass

    #gerar uma matriz com as menores distancias entre o vertice de entrada e qualquer vertice
    def matrizDjikistra(self):
        explorados = []
        d = []
        p = []
        for i in range(g.N):
            d.append(float("inf"))
            p.append(-1)
        d[self.s] = 0
        u=0
        while(not (u in explorados)):
            print(u)
            for i in range(len(d)):
                if(not(d[i] in explorados)):
                    u = d[i]
                    break
            for v in range(g.N):
                if(self.g.adjacente(u, v)):
                    if d[u] + self.g.peso(u, v) < d[v]:
                        d[v] = d[u] + self.g.peso(u, v)
                        p[v] = u
            explorados.append(u)
        mat = []
        for i in range(g.N):
            mat.append([d[i], p[i]])
        
        return mat

g = Graph(4)
g.V = ['s', 'v', 'w', 't']
#s v w t
g.graph =  [[0,1,4,0], [0,0,2,6], [0,0,0,3], [0,0,0,0]]

d = Dijkistra(g, 0)
print(d.matrizDjikistra())