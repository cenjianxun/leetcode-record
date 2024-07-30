'''
123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

# 超时
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    def oneProfit(prices):
        buy = float('inf')
        prof = 0
        for p in prices:
            if buy > p:
                buy = p
            prof = max(prof, p - buy)
        return prof

    for i in range(len(prices)):
        profit = max(profit, oneProfit(prices[:i]) + oneProfit(prices[i:]))
    return profit

# 还要看看188

'''
自己做的👍 用dp
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        dp = [[0] * L for _ in range(2)]
        buy = prices[0]
        for i in range(1, L):
            buy = min(buy, prices[i])
            dp[0][i] = max(dp[0][i-1], prices[i] - buy)
        sell = prices[-1]
        for i in range(L-2, -1, -1):
            sell = max(sell, prices[i])
            dp[1][i]  = max(dp[1][i+1], sell - prices[i])
        #print(dp)
        profit = dp[1][0]
        for i in range(L - 1):
            profit = max(profit, dp[0][i] + dp[1][i+1])
        return profit