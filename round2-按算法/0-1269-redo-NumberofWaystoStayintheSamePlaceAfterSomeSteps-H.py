'''
1269 Number of Ways to Stay in the Same Place After Some Steps

i的定义没有很坚定，一会是step了多少步，一会是除了停留的之外走了多少步
'''
def numWays(self, steps: int, arrLen: int) -> int:
    arrLen = min(arrLen, steps + 1)
    dp = [[0 for _ in range(arrLen)] for _ in range(steps + 1)]
    dp[0][0] = 1
    for i in  range(1, steps+1):
        for j in range(arrLen):
            dp[i][j] = dp[i][j] + dp[i-1][j]
            if  j >= 1:
                dp[i][j] += dp[i-1][j-1]
            if j + 1 < arrLen:
                dp[i][j] += dp[i-1][j+1]
    return dp[steps][0] % (10**9+7)