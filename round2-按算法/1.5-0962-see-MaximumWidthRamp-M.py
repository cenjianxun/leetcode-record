'''
962. Maximum Width Ramp

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
'''
'''
超时
'''
def maxWidthRamp(self, nums: List[int]) -> int:
    i, j = 0, len(nums) - 1
    n = len(nums)
    res = 0
    for i in range(n):
        j = n - 1
        while j - i > res and nums[j] < nums[i]:
            j = j - 1
        res = max(res, j - i)
    return res

'''
唔知点解的解法
'''
def maxWidthRamp(self, nums: List[int]) -> int:
    n, res = len(nums), 0
    sort_nums = sorted([(nums[i], i) for i in range(n)])
    stack = []
    print(sort_nums)
    for i in range(n):
        while stack and stack[-1][1] > sort_nums[i][1]:
            stack.pop()
        if stack:
            res = max(res, sort_nums[i][1] - stack[0][1])
        stack.append(sort_nums[i])
    return res

'''
第一想法肯定是对于每个数字都去找在它的左边，最远的那个小于等于它的数字。然后就很容易分析出，我们想要保存的是每个数字第一次出现的位置，而且依次只用保留最小的即可（数字最小才能保证距离最远）。从而就抽象出了单调栈这个数据结构。
->
抽象出单调栈：因为只用存（当前）最小的
'''