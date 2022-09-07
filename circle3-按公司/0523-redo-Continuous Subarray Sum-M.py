'''
523. Continuous Subarray Sum
Medium

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

	Input: nums = [23,2,4,6,7], k = 6
	Output: true
	Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

	Input: nums = [23,2,6,4,7], k = 6
	Output: true
	Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
	42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

	Input: nums = [23,2,6,4,7], k = 13
	Output: false

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 109
	0 <= sum(nums[i]) <= 231 - 1
	1 <= k <= 231 - 1
'''

'''
超时
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            sums = nums[i]
            for j in range(i+1, len(nums)):
                sums += nums[j]
                if sums==0 and k==0 or not sums%k:
                    return True
        return False

'''
前缀和怎么用：建立dic，和当key，index当值，如果和in dic，则xxxx

因为要找的差值需要O(1)命中，所以前缀和本身一定是key。
如果需要index做计算比如算长度，就需要map然后把index当值

1. 需要证明存储a和b对k的模成立
令b=x∗k+r1，a=y∗k+r2，
那么 r1 和 r2 分别为 b和 a 模 k 的值。
即有： b−a=(x∗k+r1)−(y∗k+r2)=(x−y)∗k+(r1−r2)。
由b−a 为 k的倍数，可以推导出r1=r2，即 b和 a 模 k 相同。
反过来由「b 和 a 模 k 相同」可推导出「b−a 为 k 的倍数」

 
2. 需要保证k不为0
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSumDic = {0:-1}
        preSum = 0
        for i in range(len(nums)):
            preSum += nums[i]
            preSum = k and preSum%k
            if preSum in preSumDic:
                if i - preSumDic[preSum] > 1:
                    return True
            else:
                preSumDic[preSum] = i
        return False