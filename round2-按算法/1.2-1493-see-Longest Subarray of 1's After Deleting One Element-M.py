'''
1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

	Input: nums = [1,1,0,1]
	Output: 3
	Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

	Input: nums = [0,1,1,1,0,1,1,0,1]
	Output: 5
	Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

	Input: nums = [1,1,1]
	Output: 2
	Explanation: You must delete one element.

Constraints:

	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
'''

'''
注意没有0的也要-1，但是要单独计算
ep：[1,1,1] 和 [1,0,0,0,0]
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        i = j = 0
        to_delete = -1
        for j in range(len(nums)):
            if to_delete == -1 and nums[j] == 0:
                to_delete = j
                continue
            if to_delete != -1 and nums[j] == 0:
                i = to_delete + 1
                to_delete = j
            if to_delete == - 1:
                res = max(res, j - i + 1)
            else:
                res = max(res, j - i)
            #print(i,j,res)
        return res if to_delete != -1 else res - 1


'''
另一个解法
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = count = 0
        l = r = 0
        while r < len(nums):
            if nums[r] == 0:
                count += 1
            if count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            r += 1
        return r - l - 1
 
