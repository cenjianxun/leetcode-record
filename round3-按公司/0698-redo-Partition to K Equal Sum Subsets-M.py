'''
698. Partition to K Equal Sum Subsets
Medium

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

	Input: nums = [4,3,2,3,5,2,1], k = 4
	Output: true
	Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

	Input: nums = [1,2,3,4], k = 3
	Output: false
 
Constraints:

	1 <= k <= nums.length <= 16
	1 <= nums[i] <= 104
	The frequency of each element is in the range [1, 4].
'''

'''
dfs+回溯

可以选择桶视角也可以选择球视角，通俗来说，我们应该尽量「少量多次」，就是说宁可多做几次选择，也不要给太大的选择空间；宁可「二选一」选 k 次，也不要「k 选一」选一次

1 <= k <= nums.length <= 16
里面循环k 外面循环nums
'''
class Solution:
    def canPartitionKSubsets(self, nums, k):
        target, m = divmod(sum(nums), k)
        if m: return False
        dp, n = [0]*k, len(nums)
        nums.sort(reverse=True)
        def dfs(i):
            if i == n:
                return len(set(dp)) == 1
            # 选择第j个桶
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and dfs(i+1):
                    return True
                dp[j] -= nums[i]
                # 这里可能index还没到nums.length，但是出现了无法凑成target的数，所以直接返回break，然后fasle就行
                if not dp[j]: break
            return False
        return nums[0] <= target and dfs(0)