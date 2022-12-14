'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''
# faster than 51.53% of Python3
def count(self, i, j, board):
    count = 0
    if i-1>=0 and j-1>=0 and board[i-1][j-1] == 1:
        count = count + 1
    if i-1>=0 and board[i-1][j] == 1:
        count = count + 1
    if i-1>=0 and j+1 < len(board[0]) and board[i-1][j+1] == 1:
        count = count + 1  
    if j-1>=0 and board[i][j-1] == 1:
        count = count + 1
    if j+1 < len(board[0]) and board[i][j+1] == 1:
        count = count + 1 
    if i+1<len(board) and j-1>=0 and board[i+1][j-1] == 1:
        count = count + 1
    if i+1<len(board) and board[i+1][j] == 1:
        count = count + 1
    if i+1<len(board) and j+1 < len(board[0]) and board[i+1][j+1] == 1:
        count = count + 1 
    return count

def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    result = ''
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            count = self.count(i,j,board)
            if board[i][j] == 1:
                if count < 2 or count > 3:
                    result = result + '0'
                else:
                    result = result + '1'
            else:
                if count == 3:
                    result = result + '1'
                else:
                    result = result + '0'
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            board[i][j] = result[i*len(board[0])+j]