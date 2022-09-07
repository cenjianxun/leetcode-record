'''
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

	Input: nums = [1,1,2,3,3,4,4,8,8]
	Output: 2

Example 2:

	Input: nums = [3,3,7,7,10,11,11]
	Output: 10
 
Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 105
'''

'''
直接看答案

需要做一些binary tree的题目

本来是需要分奇偶的情况if else
但是可以直接指定mid为偶数，利用本题的特性：如果在单个之前都是[偶]==[偶+1]，
在单个之后变成[奇]==[奇+1]，
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((l+r)//4)*2
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]