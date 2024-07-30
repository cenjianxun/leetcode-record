'''
209. Minimum Size Subarray Sum
Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

	Input: target = 7, nums = [2,3,1,2,4,3]
	Output: 2
	Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

	Input: target = 4, nums = [1,4,4]
	Output: 1

Example 3:

	Input: target = 11, nums = [1,1,1,1,1,1,1,1]
	Output: 0
 
Constraints:

	1 <= target <= 109
	1 <= nums.length <= 105
	1 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''

'''
超时
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        if sum(nums) < target:
            return 0
        for i, n in enumerate(nums):
            if n >= target: 
                return 1
            sums = [n]
            for j in range(i+1, len(nums)):
                sums.append(nums[j])
                if sum(sums) >= target:
                    res = min(res, len(sums))
                    break
        return 0 if res == float('inf') else res

'''
滑动窗口
注意 while 要j<len就行了
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = j = 0
        sums = 0
        res = float('inf')
        while j < len(nums):
            sums += nums[j]
            j += 1
            while sums >= target:
                res = min(res, j - i)
                sums -= nums[i]
                i += 1
        return 0 if res == float('inf') else res