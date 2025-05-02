class Node:

    def __init__(self, position, parent = None):
        self.position = position
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

def astar(maze, start, end):

    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)

    open_list.append(start_node)

    while open_list:

        current_node = min(open_list, key= lambda x:x.f)

        open_list.remove(current_node)
        closed_list.append(current_node)

        # gaol achieved?
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
        
            return path[::-1]
        

        # goal not achieved

        children = []

        for new_position in [(0,1),(0,-1),(1,0),(-1,0)]:
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])
            
            # check if within range
            if (node_position[0] < 0 or 
                node_position[0] >= len(maze) or 
                node_position[1] < 0 or
                node_position[1] >= len(maze[0])):
                continue

            # check if walkable
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_position, current_node)
            children.append(new_node)

        
        for child in children:

            if child in closed_list:
                continue

            child.g = child.g +1 
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g  + child.h 

            if child in open_list:
                idx = open_list.index(child)
                if open_list[idx].g > child.g:
                    continue

            open_list.append(child)

    return None


maze = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]

start = (0,0)
end = (3,3)

path = astar(maze, start, end)

if path:
    print(f"Path Found:  {path}")

else:
    print(f"Could not find path")

"""
A* SEARCH ALGORITHM THEORY:

A* (pronounced "A-star") is a pathfinding algorithm that combines the advantages of 
Dijkstra's algorithm and greedy best-first search. It uses a heuristic function to 
guide the search process toward the goal while guaranteeing the optimality of the solution.

Key components:
1. f(n) = g(n) + h(n)
   - g(n): The cost from the start node to the current node
   - h(n): A heuristic that estimates the cost from the current node to the goal
   - f(n): The total estimated cost from start to goal through the current node

2. Heuristic Functions:
   - Manhattan Distance (used in this implementation): |x1-x2| + |y1-y2|
   - Euclidean Distance: sqrt((x1-x2)² + (y1-y2)²)
   - Chebyshev Distance: max(|x1-x2|, |y1-y2|)

3. Open List: Nodes discovered but not yet evaluated (frontier)
4. Closed List: Nodes already evaluated

Properties:
- Complete: Will always find a solution if one exists
- Optimal: Finds the least-cost path when using an admissible heuristic
- Time Complexity: O(b^d) where b is the branching factor and d is the depth of the solution
- Space Complexity: O(b^d) to store all nodes in memory

Applications:
- Pathfinding in video games
- Robot navigation
- Network routing
- Puzzle solving (like the 8-puzzle, 15-puzzle)
- Any problem that can be represented as a graph search problem
"""