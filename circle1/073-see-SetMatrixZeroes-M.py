'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.
'''

# faster than 97.09% of Python3
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    store = {0:[],1:[]}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                store[0].append(i)
                store[1].append(j)
    for i in set(store[0]):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for j in set(store[1]):
        for i in range(len(matrix)):
            matrix[i][j] = 0

'''
主要是see 空间为1的解法：
用首行/首列标记本行/本列是否有0，belike：
如果某个(x, y) 为0，则映射到(x,0)=0和(0,y)=0,
那么接下来遍历首行，把所有(i,y)置0，遍历首列，把所有(x,j)置0

这里问题就是首行和首列被污染了，那么用单独两个变量标记首行和首列有没有0就行了，如果有就更新
'''