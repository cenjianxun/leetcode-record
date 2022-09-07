'''
363. Max Sum of Rectangle No Larger Than K
Hard

Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:

    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

Example 2:

    Input: matrix = [[2,2,-1]], k = 3
    Output: 3

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -100 <= matrix[i][j] <= 100
    -105 <= k <= 105

Follow up: What if the number of rows is much larger than the number of columns?
'''

'''
超时

1. 把二维压缩成1维
2. 找一维最大有题，但是如果限制最大值就只能用暴力
'''
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        maxSum = float('-inf')
        m, n = len(matrix), len(matrix[0])
        
        
        for hi in range(m):
            rowSum = [0] * n
            for lo in range(hi, m):
                for i in range(n):
                    rowSum[i] = rowSum[i] + matrix[lo][i]
                #print(rowSum)
                maxSum = max(maxSum, self.maxSumSubarray(rowSum, k, maxSum))
                if maxSum == k:
                    return k
            
        return maxSum
    
    def maxSumSubarray(self, arr, k, maxSum):
        
        for i in range(len(arr)):
            curSum = 0
            for j in range(i, len(arr)):
                curSum += arr[j]
                if curSum == k:
                    return k
                if curSum < k:
                    maxSum = max(maxSum, curSum)
                #print(i, curSum, maxSum)
        return maxSum