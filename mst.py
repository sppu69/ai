from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # For Kruskal's - store edges
        self.graph_dict = defaultdict(list)  # For Prim's - adjacency list
        
    def add_edge(self, u, v, w):
        # For Kruskal's
        self.graph.append([u, v, w])
        # For Prim's
        self.graph_dict[u].append((v, w))
        self.graph_dict[v].append((u, w))

    # Kruskal's helper functions
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0  # Index for sorted edges
        e = 0  # Index for result[]
        
        # Sort edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        print("\nKruskal's MST Construction Steps:")
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                print(f"Added edge {u}-{v} with weight {w}")

        print("\nEdges in Kruskal's MST:")
        cost = 0
        for u, v, weight in result:
            print(f"{u} -- {v} = {weight}")
            cost += weight
        print(f"Total MST Cost: {cost}")

    def prims_mst(self):
        # Pick first vertex as starting point
        start_vertex = 0
        
        # Track vertices in MST
        mst_set = set()
        
        # Track edges and costs
        edges = []
        total_cost = 0
        
        # Add start vertex
        mst_set.add(start_vertex)
        
        print("\nPrim's MST Construction Steps:")
        while len(mst_set) != self.V:
            min_edge = None
            min_cost = float('inf')
            min_vertex = None
            
            # Find minimum weight edge from vertices in MST to vertices not in MST
            for vertex in mst_set:
                for neighbor, weight in self.graph_dict[vertex]:
                    if neighbor not in mst_set and weight < min_cost:
                        min_cost = weight
                        min_edge = (vertex, neighbor)
                        min_vertex = neighbor
            
            if min_edge:
                print(f"Added edge {min_edge[0]}-{min_edge[1]} with weight {min_cost}")
                mst_set.add(min_vertex)
                edges.append(min_edge + (min_cost,))
                total_cost += min_cost
        
        print("\nEdges in Prim's MST:")
        for edge in edges:
            print(f"{edge[0]} -- {edge[1]} = {edge[2]}")
        print(f"Total MST Cost: {total_cost}")

# Test the implementation
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 5, 6)

    print("Running Kruskal's Algorithm:")
    g.kruskal_mst()
    
    print("\nRunning Prim's Algorithm:")
    g.prims_mst()