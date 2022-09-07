import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        end = [[1,2,3],[4,5,0]]
        step = 0
        visited = set()
        stack = [board]
        visited.add(str(board))
        while stack:
            next_stack = []
            # print('stack', stack)
            for s in stack:
                if s == end:
                    return step
                for one in self.addmove(s):
                    if str(one) not in visited:
                        visited.add(str(one))
                        next_stack.append(one)
            step += 1
            stack = next_stack
            # print(step, visited)
        return -1
    
    def addmove(self, board):
        stack = []
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
#                     print(board, i, j)
                    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        m, n = i + x, j + y
                        if m >= 0 and m < 2 and n >= 0 and n < 3:
                            b = copy.deepcopy(board) 
                            b[i][j], b[m][n] = b[m][n], b[i][j]
                            # print(board, i, j, m, n, b)
                            stack.append(b)
                    break
        return stack

'''
提高速度的方法果然是变1维和变str
我想到了！只是懒得写
x*num_col+y <==> [k//num_col, k%num_col]
'''