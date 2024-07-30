def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    n = len(matrix)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[n-1][i] = matrix[n-1][i]
        
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if j == 0:
                dp[i][j] = min(dp[i+1][j+1], dp[i+1][j])
            elif j == n - 1:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j-1])
            else:
                dp[i][j] = min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
            dp[i][j] = dp[i][j] + matrix[i][j]
    return min(dp[0])