'''
96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

'''
dp, 轮流当顶
'''
# faster than 53.14% of Python3
def numTrees(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    
    def getNum(n):
        count = 0
        for i in range(n):
            count = count + dp[i] * dp[n - i - 1]
        return count
        
    if n > 1:
        for i in range(2, n+1):
            dp[i] = getNum(i)
    return dp[-1]

'''
220613为什么忽然不会
x当顶的个数=x左子的个数 * x右子的个数
'''
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = dp[i] + dp[j] * dp[i - j - 1]
        return dp[-1]