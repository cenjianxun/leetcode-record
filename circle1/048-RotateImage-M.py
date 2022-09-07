'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

'''
没想到原地赋值要怎么办
'''


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    tempL = []
    l = len(matrix)
    print(matrix)
    for i in range(0, l):
        tempL.append([matrix[l-j-1][i] for j in range(0,l)])
    for i in range(0, l):
        for j in range(0, l):
            matrix[i][j] = tempL[i][j]

'''
想到了
'''
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 上下
    m, n = len(matrix), len(matrix[0])
    for j in range(n):
        i = 0
        while i < m - 1 - i:
            matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]
            i = i + 1
            
    # 斜
    for i in range(m - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]