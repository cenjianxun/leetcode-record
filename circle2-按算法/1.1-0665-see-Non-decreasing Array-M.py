'''
665. Non-decreasing Array
Medium

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

	Input: nums = [4,2,3]
	Output: true
	Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

	Input: nums = [4,2,1]
	Output: false
	Explanation: You can't get a non-decreasing array by modify at most one element.
 
Constraints:

	n == nums.length
	1 <= n <= 104
	-105 <= nums[i] <= 105
'''


'''
也是不做，边界case就难想的题
[3,4,2,3]
[5,7,1,8]
当遇到一个降序[i-1] > [i]时，有两种情况是满足条件的：
1) 是[i-1]是向上的凸起，这时需要满足[i-2] <= [i]，则抛弃[i-1]可成。【called before 非减】
2) 是[i]是向下的凹陷，这时需要满足[i-1] <= [i], 则抛弃[i]可成。【called after 非减】
这两个条件须满足i>1 & i<len-1

注意与或非的条件，是 
当 i>1 & i<len-1时，只有before非减和after非减都不满足时，才false，只要满足其中之一就可过。
当 i==1 或 i==len-1时，不用比较，都可过（只要抛弃它就可以了）。

然后再记数👆这种情况只能出现一次就行。
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                if i > 1 and nums[i-2] > nums[i] and i < len(nums) - 1 and nums[i-1] > nums[i+1]:
                    return False
                else:
                    count += 1
            if count > 1:
                return False
            i += 1
        return True