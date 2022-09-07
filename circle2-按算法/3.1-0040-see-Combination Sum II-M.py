'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

	Input: candidates = [10,1,2,7,6,1,5], target = 8
	Output: 
	[	[1,1,6],
		[1,2,5],
		[1,7],
		[2,6]
	]
	Example 2:

	Input: candidates = [2,5,2,1,2], target = 5
	Output: 
	[ 	[1,2,2],
		[5]
	]
 
Constraints:

	1 <= candidates.length <= 100
	1 <= candidates[i] <= 50
	1 <= target <= 30
'''

'''
去重的剪枝：排序的情况下：i不是第一个，且i和严格i-1的值不相等
'''
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        def dfs(cand, start):
            if sum(cand) == target:
                res.append(cand)
                return
            if sum(cand) > target:
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    break
                dfs(cand + [nums[i]], i+1)
        dfs([], 0)
        return res