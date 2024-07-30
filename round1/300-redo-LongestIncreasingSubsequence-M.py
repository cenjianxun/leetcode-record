'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''

'''
没啥好说的
'''
def lengthOfLIS(nums: List[int]) -> int:
    inc = []
    ans = []
    for i in range(len(nums)-1, -1, -1):
        index = bisect.bisect_right(ans, nums[i])  
        # print(ans, index, nums[i], i, inc)
        if index == len(ans):
            ans.append(nums[i])
            # ans_index.append(i)
            inc.append(1)
        else:
            ans.insert(index, nums[i])
            # ans_index.insert(index, i)
            inc.insert(index, i)
            inc[index] = max(inc[index+1:]) + 1
        # print(inc)
    return max(inc)

'''
动态规划
'''

def lengthOfLIS(nums):
    if not nums: return 0
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        tmax = 1
        for j in range(0, i):
            if nums[i] > nums[j]:
                tmax = max(tmax, dp[j] + 1)
        dp[i] = tmax
    return max(dp)

'''
自己做的👇
'''
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return max(dp)

'''
看看dp + 二分

注意 一开始LIS只有 一个值，所以 lo == hi，所以 while 要用 <=
'''
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [nums[0]]
        for i in range(1, len(nums)):
            lo, hi = 0, len(LIS) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if LIS[mid] < nums[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            if lo == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[lo] = nums[i]
        return len(LIS)

'''
dp[i]表示从头到i的最长长度
转移方程需要引入j，当j 在[0,i）范围内，找那个最大的+1
为什么不能用单调栈呢，因为之前的值需要用不止一次，每一轮都需要比较，当新数引入时，前面有多少个比它小的，是不定的，是不能靠前一个值来判定的。单调栈用完就pop掉了，只能用一次。
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)