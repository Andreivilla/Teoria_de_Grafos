import math
import sys
from itertools import chain, combinations

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = 0
        self.pred = node
        self.d = sys.maxsize


    def __str__(self):
        return str(self.id)
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]



class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def get_cost(self, frm, to):
        return(self.vert_dict[frm].get_weight(self.vert_dict[to]))

    def bfs(self, node):
        for v in self.vert_dict:
            self.vert_dict[v].explored = 0
        self.vert_dict[node].explored = 1
        Q = []
        Q.append(node)
        while(len(Q)>0):
            v = Q.pop(0)
            for x in self.vert_dict[v].get_connections():
                if(x.explored==0):
                    print("Exploring: ",x.get_id())
                    x.explored=1
                    Q.append(x.get_id())

    def dfs(self, node):
        for v in self.vert_dict:
            self.vert_dict[v].explored = 0
        S = []
        S = [node]+S
        while(len(S)>0):
            v = S.pop(0)
            print("Exploring: ",v)
            self.vert_dict[v].explored = 1
            for x in self.vert_dict[v].get_connections():
                if(x.explored==0):
                    S=[x.get_id()]+S

    def menor_inexplorado(self):
        menor = sys.maxsize
        for v in self.vert_dict:
            if self.vert_dict[v].explored==0 and self.vert_dict[v].d < menor:
                menorNodo = v
                menor = self.vert_dict[menorNodo].d
        return menorNodo

    def dijkstra(self, s):
        for v in self.vert_dict:
            self.vert_dict[v].explored=0
            self.vert_dict[v].pred=-1
            self.vert_dict[v].d=sys.maxsize
        self.vert_dict[s].d = 0
        expl = []
        while len(expl) != len(self.vert_dict):
            u = self.menor_inexplorado()
            expl.append(u)
            self.vert_dict[u].explored=1
            for v in self.vert_dict[u].get_connections():
                if v.explored==0 and self.vert_dict[u].d+self.vert_dict[u].get_weight(v)<v.d:
                    v.d=self.vert_dict[u].d+self.vert_dict[u].get_weight(v)
                    v.pred=u

    
    def subsets_of_size(self,size,s):
        vertices=[x for x in self.get_vertices()]
        subsets=[]
        for x in list(combinations(vertices,size)):
            if s in x:
                subsets.append(sorted(list(x)))
        return(subsets)
        
            
            
    def TSP(self, s):
        C = {}
        C[(str([s]),s)]=0
        for n in range(2,self.num_vertices+1):
            subsets=g.subsets_of_size(n,s)
            for S in subsets:
                C[(str(S),s)]=sys.maxsize
                for j in S:
                    if j!=s:
                        S_linha=S.copy()
                        S_linha.remove(j)
                        menor = sys.maxsize
                        for i in S:
                            if i!=j:
                                  if(C[(str(S_linha),i)]+self.get_cost(i,j)<menor):
                                    menor=C[(str(S_linha),i)]+self.get_cost(i,j)
                        C[(str(S),j)]=menor
                        print((str(S),j),menor)
        print("C:",C)
        menor = sys.maxsize
        for j in S:
            if j!=s:
                if(C[(str(S),j)]+self.get_cost(j,s)<menor):
                    menor=C[(str(S),j)]+self.get_cost(j,s)
                    menor_escolhido=(str(S),j)
                    final=j
        print("Destino:",s)            
        print("Custo:",menor,"Anterior:",final)
        while len(S)>1:
            menor = sys.maxsize
            S.remove(final)
            for i in S:
                if i!=final:
                   if(C[(str(S),i)]+self.get_cost(i,final)<menor):
                        menor=C[(str(S),i)]+self.get_cost(i,final)
                        menor_escolhido=(str(S),i)
                        f=i
            print("Custo:",menor,"Anterior:",f)
            final=f
                
            

            
                
            
                        
        
 
if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')

    g.add_edge('a', 'b', 10)  
    g.add_edge('a', 'c', 15)
    g.add_edge('a', 'd', 20)
    g.add_edge('b', 'c', 35)
    g.add_edge('b', 'd', 25)
    g.add_edge('c', 'd', 30)


    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

    g.TSP('a')
    
    
