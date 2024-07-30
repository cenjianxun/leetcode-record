'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
'''
看看其他解法
'''
# faster than 36.05% of Python3
# less than 53.30% of Python3
def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return 
    i = 0
    j = 1
    while j < len(nums):
        while i < len(nums) and nums[i] != 0:
            i = i + 1
        j = i + 1
        while j < len(nums) and nums[j] == 0:
            j = j + 1
        if j < len(nums):
            # print(i,j, nums)
            nums[i], nums[j] = nums[j], nums[i]


'''
while 一轮走一步
slow：移过之后，slow就指向非0的位置，条件是，slow指向非0的后一位
fast：无论如何每一轮都走一步，如果fast指向非0，那么就do sth
'''

# faster than 79.89% of Python3
def moveZeroes(nums):
    slow = fast = 0
    while fast < len(nums):
        if nums[fast]:
            if not fast == slow:
                nums[slow] = nums[fast]
                nums[fast] = 0
            slow = slow + 1
        fast = fast + 1

# faster than 79.89% of Python3
def moveZeroes(nums):
    i = 0
    for n in nums:
        if n:
            nums[i] = n
            i = i + 1
    while i < len(nums):
        nums[i] = 0
        i = i + 1



