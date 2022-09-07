'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''

# Permutation 排序


'''
思路，倒着找到第一个峰顶（这里注意有等号），然后将峰顶前一个值i-1，互换成峰顶后面所有值里，比i-1大的最小值，然后峰顶及之后的值，升序排列
inplace的题复制[:]
'''

# faster than 77.62% of Python3
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
            i = i - 1
    if i > 1:
        nums[:] = nums[:i-1] + self.helper(nums[i-1:])
    elif i == 1:
        nums[:] = self.helper(nums)
    else:
        nums.sort()
    return nums


def helper(self, nums):
    n = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[0]:
            n = i if nums[n] > nums[i] else n
            # print(n)
    nums[n], nums[0] = nums[0], nums[n]
    print(sorted(nums[1:]))
    return [nums[0]] + sorted(nums[1:])


'''
可以先排序，再交换！
'''
# faster than 93.13% of Python3
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
            i = i - 1
    h = i
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = j - 1
    if h > 0:
        for i in range(h, len(nums)):
            if nums[i] > nums[h - 1]:
                nums[i], nums[h - 1] = nums[h - 1], nums[i]
                break