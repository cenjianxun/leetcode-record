'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

	Input: nums = [1,0,-1,0,-2,2], target = 0
	Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
	Example 2:

	Input: nums = [2,2,2,2,2], target = 8
	Output: [[2,2,2,2]]

Constraints:

	1 <= nums.length <= 200
	-109 <= nums[i] <= 109
	-109 <= target <= 109
'''

'''
注意重复数字，res去重
注意b的去重 是从a+1开始不是从1开始
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for a in range(len(nums)-3):
            if a > 0 and nums[a-1] == nums[a]:
                continue
            for b in range(a+1, len(nums)-2):
                if b > a + 1 and nums[b-1] == nums[b]:
                    continue
                c, d = b+1, len(nums) - 1
                while c < d:
                    sum4 = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum4 <= target:
                        if sum4 == target:
                            res.add((nums[a], nums[b], nums[c], nums[d]))
                        c = c + 1
                    else:
                        d = d - 1
        return res