class Graph():
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.graph = [[[] for j in range(nvertices)] for i in range(nvertices)]

    #Verifica se um vértice é alcançável diretamente a partir de outro    
    def alcancavel_diretamente(self, a, b):
        if len(self.graph[a][b]) != 0:
            return True
        else:
            return False

    #Verifica se um vértice é alcançável a partir de outro
    def alcancavel(self, a, b ):
        if self.alcancavel_diretamente(a, b):
            return True
        else:
            for i in range(self.nvertices):
                if self.alcancavel_diretamente(a, i):
                    if self.alcancavel(i, b):
                        return True
            return False
    
    #verifica se existe algum parente em comum
    def ferificaParentesco(self, a, b):
        #verica o parentesco direto pai filho por exemplo
        if self.alcancavel(a, b) or self.alcancavel(b, a):
            return True
        else:#verifica se existe qualquer outro vertice q tenha parentesco em comum
            for i in range(self.nvertices):
                if self.alcancavel(i, a) and self.alcancavel(i, b):
                    return True
        return False
