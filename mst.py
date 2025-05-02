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

"""
MINIMUM SPANNING TREE (MST) ALGORITHMS THEORY:

A Minimum Spanning Tree (MST) is a subset of the edges of a connected, edge-weighted undirected graph 
that connects all the vertices together without any cycles and with the minimum possible total edge weight.

1. KRUSKAL'S ALGORITHM:
   Kruskal's algorithm builds the MST by adding edges in order of increasing weight, 
   skipping edges that would create a cycle.
   
   Steps:
   1. Sort all edges in non-decreasing order of weight
   2. Pick the smallest edge that doesn't form a cycle with the MST formed so far
   3. Repeat step 2 until there are (V-1) edges in the MST
   
   Key characteristics:
   - Uses a disjoint-set data structure (Union-Find) to detect cycles
   - Follows a greedy approach
   - Time Complexity: O(E log E) or O(E log V) for sorting edges
   - Space Complexity: O(E + V)

2. PRIM'S ALGORITHM:
   Prim's algorithm builds the MST by starting from a random vertex and 
   greedily adding the lowest weight edge that connects a vertex in the tree 
   to a vertex outside the tree.
   
   Steps:
   1. Start with a single vertex
   2. Add the minimum weight edge from tree vertices to non-tree vertices
   3. Repeat until all vertices are included
   
   Key characteristics:
   - Often implemented with a priority queue
   - Follows a greedy approach
   - Time Complexity: O(V²) with adjacency matrix, O(E log V) with binary heap
   - Space Complexity: O(V)

3. Comparison:
   - Kruskal's works well for sparse graphs (fewer edges)
   - Prim's works better for dense graphs (many edges)
   - Both guarantee an optimal MST for undirected graphs

4. Applications of MST:
   - Network design (telephone, electrical, hydraulic, TV cable, computer, road)
   - Approximation algorithms for NP-hard problems (Traveling Salesman Problem)
   - Cluster analysis
   - Image segmentation
   - Handwriting recognition
"""