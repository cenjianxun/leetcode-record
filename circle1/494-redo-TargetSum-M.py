'''
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
'''

'''
超时
'''
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    def dfs(index, cursum):
        if index == len(nums):
            return 1 if cursum == target else 0
        # mem[(index, cursum)]
        return dfs(index + 1, cursum + nums[index]) + dfs(index + 1, cursum - nums[index])
    return dfs(0, 0)

'''
加了一个存个数的就不超了
'''
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    memo = {}
    def dfs(index, cursum):
        
        if index == len(nums):
            return 1 if cursum == target else 0
        if (index, cursum) in mem:
            return memo[(index, cursum)]
        memo[(index, cursum)] = dfs(index + 1, cursum + nums[index]) + dfs(index + 1, cursum - nums[index])
        return mem[(index, cursum)]
    return dfs(0, 0)

'''
dp的内容可以为dic
'''
def findTargetSumWays(self, nums: List[int], target: int) -> int:
    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(len(nums) + 1)]
    dp[0][0] = 1
    for i, n in enumerate(nums):
        for sum_, cnt in dp[i].items():
            dp[i + 1][sum_ + n] += cnt
            dp[i + 1][sum_ - n] += cnt
    return dp[-1][target]

'''
思路拆解：dp保存之前的答案
——> 之前的答案到现在有两种，加当前和减当前
——> 所以存的内容需要是（位置，之前的每一个答案）
'''

'''
一开始错，在dfs里遍历了
for i in nums:
    dfs xxx
这里错在，入口一开始就有两个，正和负。👆相当于只有一个入口了。如果要按只有一个入口的，应该再向上找第一个正负的父节点开始

'''

def findTargetSumWays(self, nums: List[int], target: int) -> int:
    if not nums:        
        return (0 == target)

    return self.findTargetSumWays(nums[1:], target + nums[0]) + self.findTargetSumWays(nums[1:], target - nums[0])


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        preSums = {0:1}
        for n in nums:
            sums = {}
            for s in preSums:           
                sums[s+n] = sums.get(s+n, 0) + preSums[s]
                sums[s-n] = sums.get(s-n, 0) + preSums[s]
            #print(preSums, sums)
            preSums = sums
        return sums.get(target, 0)