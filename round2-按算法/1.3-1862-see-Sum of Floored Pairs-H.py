'''
1862. Sum of Floored Pairs
Hard

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

Example 1:

    Input: nums = [2,5,9]
    Output: 10
    Explanation:
    floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
    floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
    floor(5 / 2) = 2
    floor(9 / 2) = 4
    floor(9 / 5) = 1
    We calculate the floor of the division for every pair of indices in the array then sum them up.

Example 2:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 49
 
Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 105
'''

'''
不过👇
因为涉及小数，所以乘法除法不行

应该用前缀和。list的长度为nums里最大的数，index表示nums里的值
pre[i]表示前i的数的和，pre[i]-pre[i-1]表示i的和
然后商为区间值，比如4, 4-7是得1，8-11是得2
对于元素i，每次找区间
[i,i×2-1] [i×2,i×3-1] [i×3,i×4-1] ....[i×(j-1),i×j-1]之间的元素个数，倍数关系在循环中用j表示，即前面的×1×2×3；
倍数×区间内的元素总个数 = 元素i在该段区间的函数值总和；
元素i的个数×倍数×区间内的元素总个数 = 所有i在该段区间的函数值总和；
再对多段区间进行累加即可

'''
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        nums.sort()
        dpFront = [1] * len(nums)
        print(nums)
        for i in range(1, len(nums)):
            dpFront[i] = dpFront[i-1] * (nums[i] // nums[i-1]) + 1
        dpBack = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            dpBack[i] = (dpBack[i+1] + 1) * (nums[i] // nums[i+1])
        print(dpFront)
        print(dpBack)
        return sum(dpFront) + sum(dpBack)