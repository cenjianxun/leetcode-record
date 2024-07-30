''''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
看下其他解法:
也可以直接置set，如果存在就返回true
'''
def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) > len(set(nums)):
        return True
    else:
        return False

