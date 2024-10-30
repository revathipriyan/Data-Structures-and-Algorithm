
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
ROWS , COLS = len(board) , len(board[0])
def countNeighbors(r,c):
    neig = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            if((i==r and j ==c) or i<0 or j<0 or i == ROWS or j==COLS):
                continue
            if board[i][j] in [1,3]:
                neig+=1
    return neig


print(countNeighbors(1,1))