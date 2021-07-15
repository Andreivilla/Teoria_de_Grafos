class Stack:
    def __init__(self):
        self.pilha = []
        pass
    
    def tam(self):
        return len(self.pilha)
    
    def put(self, a):
        self.pilha.append(a)

    def get(self):
        return self.pilha.pop(self.tam()-1)