'''
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''

'''
遍历它同时需要给它增减值的时候使用：.copy()
'''
def canPartition(self, nums: List[int]) -> bool:
    sums = sum(nums)
    if sums & 1: return False
    nset = set([0])
    for n in nums:
        for m in nset.copy():
            nset.add(m + n)
            if sums / 2 in nset:
                return True
    return sums / 2 in nset

'''
https://www.jianshu.com/p/5f0a8a72a50f
https://www.cnblogs.com/grandyang/p/5951422.html
'''

'''
dp的index是所求之和
'''
def canPartition(self, nums: List[int]) -> bool:
    sums = sum(nums)
    if sums & 1: return False
    target = sums//2
    dp = [0] * (target + 1)
    dp[0] = 1
    for n in nums:
        i = target
        while i >= n:
            dp[i] = dp[i] | dp[i - n]
            i = i - 1
            # print(i, dp)
    return dp[target] 


'''
超时
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums) // 2

        def dfs(start, sums):
            if sums == target:
                return True
            if sums > target:
                return False
            for i in range(start, len(nums)):
                if dfs(i + 1, sums + nums[i]):
                    return True
            return False
        return dfs(0, 0)

'''
这里如果二叉树思路，节点是当前之和，分叉的因素是：选不选当前元素 ①选 ②不选
终止条件是：
curSum > target or i >= len: false
curSum == target ： true
所以递归写法：（仍然超时）
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        def dfs(i, curSum):
            if curSum == target:
                return True
            if curSum > target or i == len(nums):
                return False
            return dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)
        return dfs(0, 0)
'''
加入memo
因为这里描述一个子问题，有两个变量：curSum & i，
所以memo要么是二维的，要么key是(curSum, i)，value是状态，即True or False
另一种思路是，【在同一层】，如果当前和一样，后续分支都会一样，
所以dp[i] = set()

317的key是当前之和，只要是当前之和就都可以，所以key只是一元
这道题如果当前和为curSum，还需要判定这个值用过没有，所以要标记index
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums) // 2
        memo = {}
        def dfs(i, curSum):
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            if curSum == target:
                return True
            if curSum > target or i == len(nums):
                return False
            res = dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)
            memo[(i, curSum)] = res
            return res
        return dfs(0, 0)

'''
本题和40题的区别是 40题要返回所有情况，所以40题只能dfs
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, res = divmod(sum(nums), 2)
        if res: return False
        sums = {0}
        for n in nums:
            curSums = {n + preS for preS in sums}
            if target in curSums:
                return True
            sums = sums | curSums
        return False