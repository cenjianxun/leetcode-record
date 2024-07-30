'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''

def missingNumber(nums) -> int:
    n = len(nums)
    sumn = (n+1)*n/2
    suml = 0
    for n in nums:
        suml = suml + n
    return int(sumn-suml)

'''
还有别的办法：
1. set遍历
2. 异或： 0 ^ a = a 和 a ^ b ^ a = b
'''