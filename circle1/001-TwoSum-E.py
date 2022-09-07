'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
 
def twoSum(self, nums, target):
    m = 0
    n = len(nums) - 1
    while nums[m] + nums[n] != target:
        n = n - 1
        if m == n:
            m = m + 1
            n = len(nums) - 1
    return [m, n]
    
    
    
nums = [2,7,11,15]
target = 9
s = Solution()
s.twoSum(nums, target)

'''
新思路：一个字典：key 是当前数字，value是当前index
'''