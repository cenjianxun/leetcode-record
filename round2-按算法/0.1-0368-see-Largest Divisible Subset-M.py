'''
368. Largest Divisible Subset
Medium

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

	Input: nums = [1,2,3]
	Output: [1,2]
	Explanation: [1,3] is also accepted.
Example 2:

	Input: nums = [1,2,4,8]
	Output: [1,2,4,8]

Constraints:

	1 <= nums.length <= 1000
	1 <= nums[i] <= 2 * 109
	All the integers in nums are unique.
'''

'''
这道题的特点就在于
1. 要求的是具体的排列的结果，但仍然用dp
——> 所以可以先dp再求具体样子

2. dp的元素可能不止一个，或者说可能需要不止一个dp记录所需内容
——> 可以的。不必局限
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[1, i] for i in range(len(nums))]
        maxpair = [1, 0]
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    if dp[i][0] + 1 > dp[j][0]:
                        dp[j] = [dp[i][0] + 1, i]
                    if dp[j][0] > maxpair[0]:
                        maxpair = [dp[j][0], j]
                       
        #print(dp)
        i = maxpair[1]
        nextlen, nexti = dp[i]
        res.append(nums[i])
        while nextlen > 1:
            res.append(nums[nexti])
            nextlen, nexti = dp[nexti]
            
        return sorted(res)