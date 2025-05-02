from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # add an edge
        self.graph[u].append(v)

        #add reverse edge
        self.graph[v].append(u)

    # Original BFS (iterative)
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
    
    # New recursive BFS implementation
    def BFS_recursive(self, s):
        # create visited array and mark all unvisited
        visited = [False] * (max(self.graph)+1)
        
        # Create a queue for recursive BFS
        queue = []
        queue.append(s)
        visited[s] = True
        
        print("Recursive BFS:", end=" ")
        self.BFS_recursive_util(queue, visited)
        print()  # Add a new line at the end
    
    def BFS_recursive_util(self, queue, visited):
        # Base case - if queue is empty
        if not queue:
            return
        
        # Process the front vertex
        s = queue.pop(0)
        print(s, end=" ")
        
        # Add all unvisited neighbors to the queue
        for i in self.graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
        # Recursively process the rest of the queue
        self.BFS_recursive_util(queue, visited)

    # Original DFS (recursive)
    def DFS(self, s):
        visited = [False] * (max(self.graph)+1)
        print("Original DFS:", end=" ")
        self.DFS_util(s, visited)
        print()  # Add a new line at the end

    def DFS_util(self, s, visited):
        visited[s] = True
        print(s, end= " ")

        for i in self.graph[s]:
            if visited[i] == False:
                self.DFS_util(i, visited)
    
    # New iterative DFS implementation for comparison
    def DFS_iterative(self, s):
        # Create a visited array
        visited = [False] * (max(self.graph)+1)
        
        # Create a stack for DFS
        stack = []
        stack.append(s)
        
        print("Iterative DFS:", end=" ")
        while stack:
            # Pop a vertex from stack
            current = stack.pop()
            
            # Print and mark as visited if not already
            if not visited[current]:
                print(current, end=" ")
                visited[current] = True
            
            # Get all adjacent vertices
            # Push unvisited adjacent vertices to the stack
            # Note: We iterate in reverse order to match recursive DFS traversal
            for i in reversed(self.graph[current]):
                if not visited[i]:
                    stack.append(i)
        
        print()  # Add a new line at the end


# Testing the graph traversal algorithms
if __name__ == "__main__":
    g = Graph()

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1,4)
    g.add_edge(3,5)
    g.add_edge(2,6)

    print("Original implementations:")
    print("Iterative BFS:", end=" ")
    g.BFS(0)
    print()  # Add a new line
    
    g.DFS(0)
    
    print("\nNew implementations:")
    g.BFS_recursive(0)
    g.DFS_iterative(0)
    
    print("\nComparing different starting vertices:")
    print("Starting from vertex 2:")
    g.BFS_recursive(2)
    g.DFS(2)

"""
GRAPH TRAVERSAL ALGORITHMS THEORY:

1. BREADTH-FIRST SEARCH (BFS):
   BFS is a graph traversal algorithm that explores all the neighbor nodes at the present 
   depth before moving on to nodes at the next depth level.
   
   Key characteristics:
   - Uses a queue data structure (FIFO: First In, First Out)
   - Guarantees shortest path in unweighted graphs
   - Complete: Will find a solution if one exists
   - Time Complexity: O(V + E) where V is vertices and E is edges
   - Space Complexity: O(V) for storing the queue
   
   Applications:
   - Shortest path in unweighted graphs
   - Finding connected components
   - Testing bipartiteness of a graph
   - Finding all nodes within a connected component
   - Web crawlers
   - Social networking (finding people within N connections)

2. DEPTH-FIRST SEARCH (DFS):
   DFS is a graph traversal algorithm that explores as far as possible along each branch 
   before backtracking.
   
   Key characteristics:
   - Uses a stack data structure (LIFO: Last In, First Out) or recursion
   - Does not guarantee shortest path
   - Complete: Will find a solution if one exists, but may not be optimal
   - Time Complexity: O(V + E) where V is vertices and E is edges
   - Space Complexity: O(V) for recursion call stack
   
   Applications:
   - Topological sorting
   - Finding connected components
   - Maze generation and solving
   - Detecting cycles in graphs
   - Finding strongly connected components
   - Path finding
   
3. Comparison between BFS and DFS:
   - Memory usage: BFS requires more memory for wider graphs, DFS for deeper graphs
   - Path optimality: BFS finds shortest paths in unweighted graphs, DFS doesn't guarantee shortest paths
   - Exploration pattern: BFS explores level by level, DFS explores branch by branch
   - Implementation: BFS is typically iterative using a queue, DFS can be either recursive or iterative using a stack
"""