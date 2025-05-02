class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def is_sae(self,v, c, colours):
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colours[i] == c:
                return False
            
        return True

    def colour_graph(self, m):
        # m = #colours
        #colours assigned to each vertex
        colours = [-1] * self.V

        colours[0] = 0

        for vert in range(1, self.V):
            for c in range(m):
                colours[vert] = c
                if self.is_sae(vert, c, colours):
                    break

            if colours[vert] == -1:
                print("Bhai itne me nhi hoga")

        return colours
    
    def print_colours(self, colours):
        options = ['Red', 'Green', 'Blue', 'Yellow', 'Orange']

        for vert in range(self.V):
            print(f"Vertex {vert} ---> {options[colours[vert]]}")
    

g = Graph(5)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.graph
colour = g.colour_graph(3)

if colour is not None:
    print("\nSolution exists!")
    g.print_colours(colour)
else:
    print("No solution exists!")

"""
GRAPH COLORING THEORY:

Graph coloring is the assignment of labels (colors) to elements of a graph subject to certain constraints. 
In vertex coloring, which is implemented here, we assign colors to vertices such that no two adjacent 
vertices share the same color.

Key concepts:
1. Chromatic Number: The minimum number of colors needed to color a graph is called its chromatic number.
2. Proper Coloring: An assignment where no adjacent vertices have the same color.
3. Map Coloring: A classic application where regions of a map are colored such that no adjacent regions have the same color.

Graph coloring algorithm approaches:
1. Greedy Coloring (implemented here):
   - Assign the first available color to each vertex in sequence
   - Time Complexity: O(V²) for a graph with V vertices
   - Not guaranteed to use the minimum number of colors

2. Backtracking:
   - Try different colors for each vertex, backtrack when a conflict is detected
   - Can find the minimum number of colors needed but is exponential in time complexity

3. Other algorithms:
   - Welsh-Powell algorithm
   - DSatur algorithm
   - Genetic algorithms and other heuristic approaches

Theoretical results:
- Four Color Theorem: Any planar graph can be colored with at most four colors
- Brooks' Theorem: Any connected graph can be colored with at most Δ colors (where Δ is the maximum degree)
  except for complete graphs and odd cycles, which need Δ+1 colors

Applications:
- Map coloring
- Scheduling problems (e.g., exam timetabling)
- Register allocation in compilers
- Frequency assignment in wireless networks
- Sudoku puzzles
- Pattern matching and image segmentation

Complexity:
- Determining if a graph can be colored with k colors is NP-complete for k ≥ 3
- For k = 2 (bipartite graphs), it can be solved in linear time
- Many practical algorithms use approximations or heuristics
"""

