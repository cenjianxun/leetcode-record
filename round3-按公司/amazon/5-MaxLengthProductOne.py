'''
Given an array of only 1 and -1, find a subarray of maximum length such that the product of all the elements in the subarray is 1
like lc1567
'''

lc1567：
'''
二维动归超时
'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def f(x):
            if x > 0:
                return 1
            if x < 0:
                return -1
            return 0
        nums = list(map(f, nums))
        maxl = 0
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]
                if dp[i][j] > 0 and j - i + 1 > maxl:
                    maxl = j - i + 1
        return maxl
'''
数组中不含0:
如果数组中的-1为偶数位，那么答案就是数组的长度，
如果数组中的-1为奇数位，那么答案就是最后一个负数位置的前区间len1和第一个负数位置的后区间len2当中最大的一个。
 
含0：
用0分段
'''

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        start = 0
        nums.append(0)
        maxl = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxl = max(maxl, self.maxLenWithoutZero(nums[start:i]))
                if i + 1 < len(nums):
                    start = i + 1
        return maxl
    
    def maxLenWithoutZero(self, nums):
        negCount = 0
        firstNeg, lastNeg = -1, -1
        for i in range(len(nums)):
            if nums[i] < 0:
                negCount += 1
                if firstNeg == -1:
                    firstNeg = i
        if not negCount%2:
            return len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < 0 and lastNeg == -1:
                lastNeg = i
                break
        return max(len(nums)-1-firstNeg, lastNeg)