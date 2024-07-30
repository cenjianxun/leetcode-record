'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

# faster than 5.03% of Python3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    store = {(i,j)}
                    if self.search(board, i, j, word, store):
                        return True
        return False
    
    def search(self, board, i, j, s, store):
        if not s:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != s[0]:
            return False
        flag = False
 
        # print( i, j, s, store)
        for x, y in zip((-1,1,0,0),(0,0,-1,1)):
            if (i+x, j+y) not in store:
                flag = flag or self.search(board, i+x, j+y, s[1:], store | {(i+x,j+y)})
        return flag

'''
1. !! 恢复现场，可以再循环之后，再赋值回去，不用另开store了
2. 如果是true就直接返回，不用等待了
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.search(board, i, j, word ):
                        return True
        return False
    
    def search(self, board, i, j, s):
        if not s:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != s[0]:
            return False
        board[i][j] = ''
        # print( i, j, s, store)
        # if search(i+1, j, s[1:]) or search(i, j+1, s[1:]) or search(i-1, j, s[1:]) or search(i, j-1, s[1:]): 这样竟然快1000多ms
        for x, y in zip((-1,1,0,0),(0,0,-1,1)):
            if self.search(board, i+x, j+y, s[1:]):
                return True
        board[i][j] = s[0]
        return False

'''
存起横竖快90% 怎么会这样
在方块里遍历要考虑重复路径的问题：标记
在helper里如何return：还是写上吧
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return 
        m, n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.helper(board, m,n,i, j, word[1:]):
                    return True
        return False 
    
    def helper(self, board, m,n,i, j, w):
        if not w:
            return True

        temp = board[i][j]
        board[i][j] = ''
        for x, y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            border = 0 <= x < m and 0 <= y < n
            if border and board[x][y] == w[0] and self.helper(board, m,n,x, y, w[1:]):
                return True
        board[i][j] = temp 
        return False