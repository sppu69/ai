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
    
