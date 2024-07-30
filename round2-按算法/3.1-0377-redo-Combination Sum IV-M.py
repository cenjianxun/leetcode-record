'''
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:

	Input: nums = [1,2,3], target = 4
	Output: 7
	Explanation:
	The possible combination ways are:
	(1, 1, 1, 1)
	(1, 1, 2)
	(1, 2, 1)
	(1, 3)
	(2, 1, 1)
	(2, 2)
	(3, 1)
	Note that different sequences are counted as different combinations.

Example 2:

	Input: nums = [9], target = 3
	Output: 0
 
Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= 1000
	All the elements of nums are unique.
	1 <= target <= 1000
 
Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
'''

'''
超时
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(sums, res):
            if sums >= target:
                if sums == target:
                    res += 1
                return res
            for i in range(len(nums)):
                res = dfs(sums + nums[i], res)
            return res
        res = dfs(0, 0)
        return res
    
'''
如果每轮遍历都是从头开始，那么可以不用内层函数，直接退行用本函数（仍然超时）
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        if target < 0:
            return 0
        if target == 0:
            return 1
        for n in nums:
            res += self.combinationSum4(nums, target - n)
        return res

'''
和之前的区别是，不在命中过程中累加，而是计为1，另设0，在遍历的时候递归调用累加。
那么初始定义{0：1}的意义就是，当rest=0时，需要标为1即算一个
其余就按记忆化存储，当存在时直接return，不存在时计算结果然后赋值
'''
# faster than 17.41% of Python3
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0:1}
        def dfs(rest):
            if rest < 0:
                return 0
            if rest in memo:
                return memo[rest]
            res = 0
            for n in nums:
                res += dfs(rest - n)
            memo[rest] = res
            return res
        return dfs(target)

'''
总的种类，等于每一个值的所有可能种类之和
那么dfs(target) 就 = sum([dp[target-n] for n in nums])
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]
        return dp[-1]

  
