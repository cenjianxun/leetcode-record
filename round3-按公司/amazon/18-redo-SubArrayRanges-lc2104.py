'''
2104. Sum of Subarray Ranges

You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

	Input: nums = [1,2,3]
	Output: 4
	Explanation: The 6 subarrays of nums are the following:
	[1], range = largest - smallest = 1 - 1 = 0 
	[2], range = 2 - 2 = 0
	[3], range = 3 - 3 = 0
	[1,2], range = 2 - 1 = 1
	[2,3], range = 3 - 2 = 1
	[1,2,3], range = 3 - 1 = 2
	So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:

	Input: nums = [1,3,3]
	Output: 4
	Explanation: The 6 subarrays of nums are the following:
	[1], range = largest - smallest = 1 - 1 = 0
	[3], range = 3 - 3 = 0
	[3], range = 3 - 3 = 0
	[1,3], range = 3 - 1 = 2
	[3,3], range = 3 - 3 = 0
	[1,3,3], range = 3 - 1 = 2
	So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

Example 3:

	Input: nums = [4,-2,-3,4,1]
	Output: 59
	Explanation: The sum of all subarray ranges of nums is 59.
 
Constraints:

	1 <= nums.length <= 1000
	-109 <= nums[i] <= 109

Follow-up: Could you find a solution with O(n) time complexity?
'''

'''
超时
'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            j = i + 1
            largest = smallest = nums[i]
            while j < len(nums):
                largest = max(nums[j], largest)
                smallest = min(nums[j], smallest)
                res += largest - smallest
                j += 1
        return res

'''
单调栈

注意点： 
nums.append(0)
while 判定有一个 i如果是最右边，就直接进入循环
while 里面有一个 i如果是最左边，边缘就当是-1，所以是-（-1）
'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        min_stack, max_stack = [], []
        n = len(nums)
        nums.append(0)

        for i, num in enumerate(nums):
            print(i)
            while min_stack and (i == n or num < nums[min_stack[-1]]):
                top = min_stack.pop()
                starts = top - min_stack[-1] if min_stack else top + 1
                ends = i - top
                res -= starts * ends * nums[top]
                print(min_stack, starts, ends)
            min_stack.append(i)
            
            while max_stack and (i == n or num > nums[max_stack[-1]]):
                top = max_stack.pop()
                starts = top - max_stack[-1] if max_stack else top + 1
                ends = i - top
                res += starts * ends * nums[top]
                
            max_stack.append(i)
        
        return res