'''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

	Input: nums = [1,2,2]
	Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

	Input: nums = [0]
	Output: [[],[0]]
 
Constraints:

	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
'''

'''
这道题的去重和前面的不同。
它是一层一层的，如果重复，那么只有最新一层有效，再往前，就和前一个重复的值效果一样。
所以需要记录上一层的值
1,2,3,3,4 
[], [1], [2],[1,2] #before
[3],[1,3],[2,3],[1,2,3] # 上一层



如果纵着做就是continue 但是复杂
1,2,3,3,4 
[],
[1],[1,2],[1,3],[1,4],[1,2,3],[1,2,4],[1,3,3],[1,2,3,3],[1,2,3,4] 
[2],[2,3],[2,3,4]
[3],[3,4]
[4],
 


'''
# faster than 99.90% of Python3
class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res