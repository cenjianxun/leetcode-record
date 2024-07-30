'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
 
Example 1:

	Input: nums = [-1,2,1,-4], target = 1
	Output: 2
	Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
	Example 2:

	Input: nums = [0,0,0], target = 1
	Output: 0

Constraints:

	3 <= nums.length <= 1000
	-1000 <= nums[i] <= 1000
	-104 <= target <= 104
'''

'''
为什么只有我超时
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        res = sum[nums[:3]]
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1 
            while j < k:
                #print(i, j, k)
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(sums - target) < abs(res - target):
                    res = sums
                if sums < target:
                    j = j + 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                else:
                    k = k - 1
                    while j < k and nums[k] == nums[k+1]:
                        k = k - 1           
        return res


'''
k数和
好方法啊
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current
        
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest