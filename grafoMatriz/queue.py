class Queue:
    def __init__(self,):
        self.fila = []
        pass
    
    def tam(self):
        return len(self.fila)

    def put(self, a):
        self.fila.append(a)
    
    def get(self):
        return self.fila.pop(0)