from dfs import Dfs
from graph import Graph

class Euleriano:
    def __init__(self, g):
        self.g = g

    def isEuleriano(self):
        impares = 0
        for i in range(g.tam()):
            if self.g.grau(i)%2 ==0:
                impares += 1
        
        if impares == 0:
            return "Tem ciclo Euleriano"
        
        if impares == 2:
            return "Tem caminho Euleriano"
        
        if impares > 2:
            return "Não é euleriano"

    def isConected(self):
        explorados = []
        for i in range(g.tam()):
            explorados.append(False)
        u = -1
        for i in range(g.tam()):
            if self.g.grau(i) > 0:
                u = i
                break
        
        dfs = Dfs(u)
        listaDfs = dfs.graphDfs()#retorna a lista de busca em dfs

        for i in range(g.tam()):
            if i not in listaDfs:
                return False
        
        return False