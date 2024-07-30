'''
673. Number of Longest Increasing Subsequence
Medium

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

	Input: nums = [1,3,5,4,7]
	Output: 2
	Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

	Input: nums = [2,2,2,2,2]
	Output: 5
	Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 
Constraints:

	1 <= nums.length <= 2000
	-106 <= nums[i] <= 106
'''

'''
不会。300升级版
需要能想到第二个dp：count，以及count的转移方程
if dp[j] + 1 == dp[j]: count[i] += count[j]
if dp[j] + 1 > dp[j]: count[i] = count[j]

以及最后还要遍历一遍dp

and see 树状dp
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp, count = [1] * len(nums), [1] * len(nums)
        longest = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    #print(nums[i], nums[j], dp[i], dp[j]+1)
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            longest = max(longest, dp[i])
        result = 0
        for i in range(len(nums)):
            if dp[i] == longest:
                result += count[i]
        return result