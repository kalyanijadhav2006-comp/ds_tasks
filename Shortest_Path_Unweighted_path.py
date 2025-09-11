from collections import deque, defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def shortestPath(self, start, end):
        visited = [False] * self.V
        distance = [-1] * self.V
        queue = deque([start])

        visited[start] = True
        distance[start] = 0

        while queue:
            node = queue.popleft()
            if node == end:
                return distance[node]

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)

        return -1 
    

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 0)

print("Shortest path length from 0 to 3:", g.shortestPath(0, 3)) 