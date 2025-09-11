from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.isCyclicUtil(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, -1):
                    return True
        return False



g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

print("Does graph contain cycle?", g.isCyclic())