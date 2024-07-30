'''
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Medium

Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:

    Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
    Output: 2
    Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

    Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
    Output: 0
 
Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 300
    0 <= mat[i][j] <= 104
    0 <= threshold <= 105
'''

'''
注意的点是max_side不会缩小（否则会超时）
m+1,n+1这样考虑每次参与计算的max_side是最大边长+1
所以判断之后直接+1
'''
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        max_side = 0
        m, n = len(mat), len(mat[0])
        preSum = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                preSum[i+1][j+1] = preSum[i+1][j] + preSum[i][j+1] - preSum[i][j] + mat[i][j]
        print(preSum)
        for i in range(m):
            for j in range(n):
                if min(i, j) >= max_side:
                    area = preSum[i+1][j+1] - preSum[i+1][j-max_side] - preSum[i-max_side][j+1] + preSum[i-max_side][j-max_side]
                    print(max_side, i,j,area) 
                    if area <= threshold:
                        max_side += 1
                     
        return max_side