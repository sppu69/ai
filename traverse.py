from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def add_edge(self, u, v):
        # add an edge
        self.graph[u].append(v)

        #add reverse edge
        self.graph[v].append(u)


    def BFS(self, s):
        
        # create visited array and mark all unvisited
        visited = [False] * (max(self.graph)+1)

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self,s):

        visited = [False] * (max(self.graph)+1)
        self.DFS_util(s,visited)

    def DFS_util(self, s, visited):

        visited[s] = True
        print(s, end= " ")

        for i in self.graph[s]:
            if visited[i] == False:
                self.DFS_util(i,visited)


g = Graph()


g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(2,6)

print(g.BFS(0))
print(g.DFS(0))