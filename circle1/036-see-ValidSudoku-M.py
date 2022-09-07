'''
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''

'''
3x3的部分要怎么遍历
'''

def isValidSudoku(board):
    for i in range(0, 9):
        s1 = board[i]
        s1 = list(''.join(s1).replace('.',''))
        if len(s1) > len(set(s1)):
            return False
        s2 = [board[j][i] for j in range(9)]
        s2 = list(''.join(s2).replace('.',''))
        if len(s2) > len(set(s2)):
            return False
        
    for k in range(0,9,3):
        for i in range(0, 9):
            print(board[i][k:k+3])
            if not i%3:
                s = []
            s.extend(board[i][k:k+3])
            if i%3 == 2:
                s = list(''.join(s).replace('.',''))
                if len(s) > len(set(s)):
                    return False
    return True

board = [[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]

r = isValidSudoku(board)
print(r)

'''
一个超级简单的方法：
思想就是：如果要跨越3，那么可以用i/3来确定
(i, c),(c, j) <—— 为了区分横坐标和纵坐标，颠倒一下
'''
def isValidSudoku(board):
    stack = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            c = board[i][j]
            if c != '.':
                stack = stack + [(i, c),(c, j),(i//3, j//3, c)]
    return len(stack) == len(set(stack))