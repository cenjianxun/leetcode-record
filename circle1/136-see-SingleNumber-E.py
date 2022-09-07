'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

'''
慢 faster than 12.70% of Python3
'''

def singleNumber(nums: List[int]) -> int:
    stack = []
    for n in nums:
        if not n in stack:
            stack.append(n)
        else:
            stack.remove(n)
    return stack[0]

'''
异或：两个相同的值，异或=0
'''
def singleNumber(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res = res ^ n
    return res