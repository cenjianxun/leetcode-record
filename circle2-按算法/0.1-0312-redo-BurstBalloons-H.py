'''
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''

'''
三个点：
1. dp的定义：dp[i][j] 表示i和j中间的最佳值
→ i和j本身都不取
→ 给nums加左右边界值
2. 转移方程怎么写：dp[i][j] = 
dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
→ 【假设最后留下来的是k】，需要先把i-k和k-j都戳爆
→ 戳爆后 要乘的刚好是num[i]和num[j]
3.遍历的顺序，看最终要求的在矩形哪个地方
'''
def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i + 2, len(nums)):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
                # print(dp)

    return dp[0][-1]

'''
下面练习遍历 这俩都超时
'''

def maxCoins(self, nums: List[int]) -> int:
    self.coins = 0
    mem = {}
    def dfs(left, right, n, coins):
        # if not left and not right:
        #     self.coins = max(self.coins, coins + n)
        #     return 
        L = left + right
        if len(L) == 1:
            coins = coins + L[0] * n + max(L[0], n)
            self.coins = max(self.coins, coins)
            return 
        if not left:
            coins = coins + n * right[0]
        elif not right:
            coins = coins + n * left[-1]
        else:
            coins = coins + right[0] * n * left[-1]
        
        for i in range(len(L)):
            dfs(L[:i], L[i+1:], L[i], coins)
            
    for i in range(len(nums)):
        dfs(nums[:i], nums[i+1:], nums[i], 0)
    return self.coins

# ↓ ↓ ↓ 变成在循环里拆解
def maxCoins(self, nums: List[int]) -> int:
    self.coins = 0
    # mem = {}
    def dfs(nums, coins):

        if not nums:
            self.coins = max(self.coins, coins)
            return 
        
        for i in range(len(nums)):
            point = nums[i] 
            if i > 0:
                point = point * nums[i - 1]
            if i < len(nums) - 1:
                point = point * nums[i + 1]
            dfs(nums[:i] + nums[i+1:], coins + point)

    dfs(nums, 0)
    return self.coins


#====

'''
dfs （加memo还是）超时版
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def helper(nums):
            if tuple(nums) in memo:
                return memo[tuple(nums)]
            coins = 0
            for i in range(len(nums)):
                coin = nums[i]
                new_nums = nums[:i] + nums[i+1:]
                if i > 0:
                    coin *= nums[i-1]
                if i < len(nums) - 1:
                    coin *= nums[i+1]
                coins = max(coins, coin + helper(new_nums))
            memo[tuple(nums)] = coins
            return memo[tuple(nums)]
        return helper(nums)