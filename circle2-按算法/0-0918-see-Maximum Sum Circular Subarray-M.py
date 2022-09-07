'''
918. Maximum Sum Circular Subarray
Medium

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

    Input: nums = [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3.

Example 2:

    Input: nums = [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

    Input: nums = [-3,-2,-3]
    Output: -2
    Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

    n == nums.length
    1 <= n <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
'''
'''
一个list里的最大子序和和最小子序和分情况：
1. 相交：
    ①部分相交：相交子序列和为0
    ②包含：数组中元素均非正or均非负
    ③完全重合：数组长度为1，or数组所有元素都为0
2. 相连
3. 分离：相离子序和为0

符合【sum = 最大子序和 + 最小子序和】 的情况：【除了 包含 和 完全重合】
 

另外一种思路：为什么要单独分情况：
是初始假设max一定>=0, 包含了选取元素为0个的情况。但是需要至少一个元素，所以是边界情况
'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        L = len(nums)
        preMax = preMin = nums[0]
        sumMax = sumMin = nums[0]
        for i in range(1, L):
            preMax = max(nums[i], nums[i] + preMax)
            sumMax = max(sumMax, preMax)
            preMin = min(nums[i], nums[i] + preMin)
            sumMin = min(sumMin, preMin)
        if sumMax < 0:
            return max(nums)
        else:
            return max(sumMax, sum(nums)-sumMin)