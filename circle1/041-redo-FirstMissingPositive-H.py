'''
Given an unsorted integer array nums, find the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

'''
把位置利用起来

位置是从0往后的
先把值可以填到相应位置的值填到相应位置，那么第一个不对应的就是所求
'''

def firstMissingPositive(nums) -> int:
    if len(nums) == 1:
        if nums[0] == 1:
            return 2
        else:
            return 1
    i = 0 
    while i < len(nums):
        print(nums)
        if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
            print(i, nums[i], nums[nums[i]-1])
            nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        else:
            i = i + 1

    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

n = [3,4,-1,1]
r = firstMissingPositive(n)
print(r)


'''
找从0开始的最小的连续值，记录边界。如果这个区域覆盖的位置比1小或者比2大，就return 1，
如果覆盖了1，就return 右边+1
注意的地方就是，初始值设定，因为选最小值，所以选了无限大，那么左边界需要注意，<2或者，还有一个情况就是根本没有赋值，因为这个规则把<0的封死了，所以这个时候左值不会赋值，那么它会是极大值
'''

# faster than 57.63% of Python3

def firstMissingPositive(self, nums: List[int]) -> int:
    maxnum = minnum = float('inf')
    nums = set(nums)

    for n in nums:
        if n > 0: 
            # 求最小的连续值，好方法
            if not n + 1 in nums and maxnum > n:
                maxnum = n
            if not n - 1 in nums and minnum > n:
                minnum = n
    print(minnum, maxnum)
    if minnum > maxnum or minnum < 2:
        return maxnum + 1
    else:
        return 1


# faster than 5.01% of Python3
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        min_pos, max_pos = float('inf'), 0
        for n in nums:
            if n > 0:
                max_pos = max(max_pos, n)
                min_pos = min(min_pos, n)
        if min_pos != 1:
            return 1
        for i in range(min_pos, max_pos + 1):
            if i not in nums:
                return i
        return max_pos + 1