'''
491. Increasing Subsequences
Medium

Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

Example 1:

	Input: nums = [4,6,7,7]
	Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

	Input: nums = [4,4,3,2,1]
	Output: [[4,4]]

Constraints:

	1 <= nums.length <= 15
	-100 <= nums[i] <= 100
'''

'''
为什么复杂

噢 为什么要set去重：
因为4677里面有两个重复，467就有两个，如果是4678的话，就是467和468，所以要去重
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        
        def dfs(k, sub):
            #print(k, sub, self.res)
            for i in range(k, len(nums)):
                if sub and sub[-1] <= nums[i]:
                    self.res.add(tuple(sub+[nums[i]]))
                if not sub or sub[-1] <= nums[i]:
                    dfs(i+1, sub+[nums[i]])
                #print(i, k, sub, self.res)
        dfs(0, [])
        return self.res