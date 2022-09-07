'''
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''


'''
定义迷惑 1什么叫围住 2怎么叫连起来：
结果就是只不算和边边联通的，连通只算直上直下

* 注意横竖的边界

（dnf）？
'''

'''
不用visited的set，直接在原board上标其他值
'''

def search(i, j, board):
    
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return board
    if board[i][j] == 'O':
        board[i][j] = 'C'
        board = self.search(i-1, j, board)
        board = self.search(i+1, j, board)
        board = self.search(i, j-1, board)
        board = self.search(i, j+1, board)
        # print(i,j,board)
    return board

def solve( board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return board
    for j in range(0, len(board[0])):
        print((0,j),(len(board)-1,j))
        board = search(0, j, board)
        board = search(len(board)-1, j, board)
    # print(board)
    for i in range(0, len(board)):
        board = search(i, 0, board)
        board = search(i, len(board[0])-1, board)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 'C':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'