'''
581. Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
'''

'''
好莫名其妙的题
'''
def findUnsortedSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    res = []
    sortNums = sorted(nums)
    print(nums)
    print(sortNums)
    for i in range(n):
        if nums[i] != sortNums[i]:
            res.append(i)
    return res[-1] - res[0] + 1 if res else 0

'''
屁 很好的题 并不会做
[1,3,2,2,2]
[1,3,2,3,3]
'''
 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        return 0 if right == -1 else right - left + 1