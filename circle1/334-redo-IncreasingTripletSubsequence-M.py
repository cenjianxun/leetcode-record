'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

'''
1. 这样的数组必定存在两个相邻的nums[i]<nums[j]，而且不是最后两个
2. 当k<i时，不用更新j，是因为新一轮 相当于两个个选择，①k<j，j就会被更新上来。 ②k>j，此时直接是true，此时成组的是前i，j和k，因为k比j大，j又比前i大。
'''
# faster than 42.65% of Python
# less than 59.50% of Python3
def increasingTriplet(nums: List[int]) -> bool:
    i, j = 0, 1
    while i < len(nums) and j < len(nums) and nums[i] >= nums[j]:
        i = i + 1
        j = j + 1
    k = j + 1
    while k < len(nums):
        if nums[k] > nums[j]:
            return True
        elif nums[k] > nums[i]:
            j = k
        else:
            i = k
            # j = i+1 ！！不能有这行
        k = k + 1


# faster than 85.22% of Python3
def increasingTriplet(nums: List[int]) -> bool:
    small = 0xffffffff
    large = 0xffffffff
    for n in nums:
        if n <= small:
            small = n
        elif n <= large:
            large = n
        else:
            return True
    return False


# 正无穷 float("inf")
# 负无穷 float("-inf")

def increasingTriplet(nums: List[int]) -> bool:
    import bisect
    res = []
    for n in nums:
        index = bisect.bisect_left(res, n)
        if index == len(res):
            res.append(n)
        else:
            res[index] = n
        if len(res) == 3:
            return True
    return False