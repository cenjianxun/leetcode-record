'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

	Input: nums = [1,0,-1,0,-2,2], target = 0
	Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
	Example 2:

	Input: nums = [2,2,2,2,2], target = 8
	Output: [[2,2,2,2]]

Constraints:

	1 <= nums.length <= 200
	-109 <= nums[i] <= 109
	-109 <= target <= 109
'''

'''
注意重复数字，res去重
注意b的去重 是从a+1开始不是从1开始
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for a in range(len(nums)-3):
            if a > 0 and nums[a-1] == nums[a]:
                continue
            for b in range(a+1, len(nums)-2):
                if b > a + 1 and nums[b-1] == nums[b]:
                    continue
                c, d = b+1, len(nums) - 1
                while c < d:
                    sum4 = nums[a] + nums[b] + nums[c] + nums[d]
                    if sum4 <= target:
                        if sum4 == target:
                            res.add((nums[a], nums[b], nums[c], nums[d]))
                        c = c + 1
                    else:
                        d = d - 1
        return res

'''
n数之和：
dfs

n==2处用指针而不是map，是因为要去重。
而且已经排序了，用map就相当于又打乱了排序
'''
def fourSum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 4, [], results)
    return results

def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return