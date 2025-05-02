N = 4

board = [[0 for _ in range(N)] for _ in range(N)]


def _print(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col, N):
    
    # column check 
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # left diagonal
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] ==1:
            return False
        
    # right diagonal
    for i,j in zip(range(row,-1,-1),range(col,N)):
        if board[i][j] ==1:
            return False
                   
    return True

def solve_nqueen(board, row, N) -> bool:
    # terminating condition
    if row>= N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            # place the queen 
            board[row][col] = 1
            # print the board
            _print(board)
            # recur for next states
            if solve_nqueen(board, row+1, N):
                # if the state is successful, return true
                
                return True
            # state failed, remove the queen
            board[row][col] = 0


    return False


if solve_nqueen(board, 0,N):
    _print(board)
else: 
    print("Ille")

"""
N-QUEENS PROBLEM THEORY:

The N-Queens problem is a classic combinatorial problem that asks how to place N chess queens 
on an N×N chessboard so that no two queens threaten each other. In chess, a queen can attack 
horizontally, vertically, and diagonally.

Key aspects of the problem:
1. Each row must contain exactly one queen
2. Each column must contain exactly one queen
3. No two queens can share the same diagonal

Solution approach using Backtracking:
- Place queens one by one in different columns, starting from the leftmost column
- When placing a queen in a column, check if it's safe from attack by already placed queens
- If a safe position is found, mark this position as part of the solution
- If placing a queen doesn't lead to a solution, remove the queen and try other rows
- If all rows are tried and no solution is found for a column, return false

Properties:
- The problem has solutions for all N except N=2 and N=3
- For N=1, there is 1 solution
- For N=4, there are 2 solutions
- For N=8, there are 92 solutions

Time Complexity: O(N!) in the worst case, but often better in practice due to pruning
Space Complexity: O(N) for recursion call stack plus O(N²) for the board

Optimizations:
- Using a 1D array instead of a 2D board
- Bitwise operations
- Symmetry considerations
- Forward checking and constraint propagation

Applications:
- Combinatorial optimization
- Constraint satisfaction problems
- Demonstration of backtracking algorithms
- Parallel processing and multiprocessor scheduling
"""
