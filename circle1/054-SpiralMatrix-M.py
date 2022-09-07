'''
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.
'''
# faster than 6.17% of Python3
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    flag = 0
    res = []
    while left <= right and up <= down:
        if flag%4 == 0:
            if left <= right:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                flag = flag + 1
                up = up + 1
                # print(left, right, up, down)
                # print(res)
            else:
                return res
        if flag%4 == 1:
            if up <= down:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                flag = flag + 1
                right = right - 1
                # print(left, right, up, down)
                # print(res)
            else:
                return res
        if flag%4 == 2:
            if left <= right:
                for i in  range(right, left - 1, -1):
                    res.append(matrix[down][i])
                flag = flag + 1
                down = down - 1
                # print(left, right, up, down)
                # print(res)
            else:
                return res
        if flag%4 == 3:
            if up <= down:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                flag = flag + 1
                left = left + 1
                # print(left, right, up, down)
                # print(res)
            else:
                return res
    return res


'''
另一种
'''
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    flag = 0
    res = []
    step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    while len(res) < len(matrix)* len(matrix[0]):
        res.append(matrix[x][y])
        if flag == 0 and y == right:
            flag = flag + 1
            up = up + 1
        elif flag == 1 and x == down :
            flag = flag + 1
            right = right - 1
        elif flag == 2 and y == left :
            flag = flag + 1
            down = down - 1
        elif flag == 3 and x == up:
            flag = flag + 1
            left = left + 1
        flag = flag%4
        x = x + step[flag][0]
        y = y + step[flag][1]
        
    return res