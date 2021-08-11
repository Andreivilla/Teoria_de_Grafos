from graph import Graph
class TravellingSalesman:
    def __init__(self, g):
        self.g = g

    #m = matiz de ajacencia
    #s = vertice de inicio (0 <= s < n)
    def tsp(self, s):
        m = self.g.graph
        n = len(m) #trocar esse m pelamatriz do grapho g

        #inicializar tabela memo
        #fill table with floatr('inf')
        memo = [[float('inf') for j in range(2**n)] for i in range(n)]

        self.setup(m, memo, s, n)
        self.solve(m , memo, s, n)

        minCost = self.findMinCost(m, memo, s, n)
        tour = self.findOptimalTour(m, memo, s, n)

        return (minCost, tour)
    
    def setup(self, m, memo, s, n):
        for i in range(n):
            if i == s: continue
            memo[i][1 << s | 1 << i] = m[s][i]

    def notIn(self, i, subset):
        return((1 << i) & subset) == 0


    def solve(self, m, memo, s, n):
        for r in range(3, n):
            #combinations
            for subset in self.combinations(r, n):
                if self.notIn(s, subset): continue
                for nxt in range(n):
                    if nxt == s or self.notIn(nxt, subset): continue
                    #substate sem next node
                    state = subset ^(1 << nxt)
                    minDist = float('inf')
                    for e in range(n):
                        if e == s or e == nxt or self.notIn(e, subset): continue
                        newDistance = memo[e][state] + m[e][nxt]
                        if newDistance < minDist: minDist = newDistance
                    memo[nxt][subset] = minDist

    def combinations(self, r, n):
        subset = []
        self.combinationsAux(0, 0, r, n, subset)
        return subset

    def combinationsAux(self, st, at, r, n, subset):
        if r == 0:
            subset.append(st)
        else:
            for i in range(at, n):
                st = st | (1 << i)
                self.combinationsAux(st, i+1, r-1, n, subset)
                st = st & ~(1 << i)
    
    def findMinCost(self, m, memo, s, n):
        end_state = (1 << n) - 1
        minTourCost = float('inf')

        for e in range(n):
            if e == s: continue

            tourCost = memo[e][end_state] + m[e][s]
            
            if tourCost < minTourCost:
                minTourCost = tourCost
                
        return minTourCost


    def findOptimalTour(self, m, memo, s, n):
        lastIndex = s
        state = (1<<n) - 1
        tour = [float('inf') for i in range(n+1)]
        
        for i in range(n-1, 0, -1):
            index = -1
            for j in range(n):
                if j == s or self.notIn(j, state): continue
                if index == -1:
                    index = j
                
                prevDist = memo[index][state] + m[index][lastIndex]
                newDist = memo[j][state] + m[j][lastIndex]
                
                if(newDist < prevDist):
                    index = j
            tour[i] = index
            state = state ^ (1 << index)
            lastIndex = index

        tour[0] = s
        tour[n] = s
        return tour


g = Graph(4)
g.graph =  [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

tr = TravellingSalesman(g)

print(tr.tsp(0))

