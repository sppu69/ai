N = 7
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
            # recur for next states
            if solve_nqueen(board, row+1, N):
                return True
            # state failed, remove the queen
            board[row][col] = 0


    return False


if solve_nqueen(board, 0,N):
    _print(board)
else: 
    print("Ille")
