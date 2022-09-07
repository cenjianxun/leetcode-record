'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

'''
论一下迭代和动规的区别
上为动规 下为迭代
迭代是从大到小，从后往前：先想获得 i 位置的结果 ，然后分解成求解 i - 1 位置的结果 和 i - 2 位置的结果。这就是从顶向下
递归是从底向上：先求 i - 1 位置的结果 和 i - 2 位置的结果，再求 i 位置的结果不是也行吗？对！这就是 动态规划，它的思想是从底向上。
dp[i] 表示从左到右的第 i 个位置能偷多少金额
'''
def rob(nums: List[int]) -> int:
    dp = [0] * (len(nums))
    if not nums:
        return 0
    if len(nums) < 3:
        return max(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.dfs(nums, len(nums) - 1)
    
    # 在第 i 个房间之前（包括 i）能获取的最大收益
    def dfs(self, nums, i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        return max(self.dfs(nums, i - 1), self.dfs(nums, i - 2) + nums[i])
