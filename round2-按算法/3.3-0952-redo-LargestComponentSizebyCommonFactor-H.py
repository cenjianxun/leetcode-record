'''
952. Largest Component Size by Common Factor

You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.
'''

'''
这道题redo的意义在于提速：
1. 求约数: 遍历上限是x**0.5 + 1
2. 给UF加平衡因子，size
3. 重要。在判断是否可以union的时候，不一定要把每个元素的条件值全求出来再求交集，
可以转化为求这些条件值的union，即遍历一次，边求每个元素条件值边判断是否union
这里要注意parents的长度就是条件值个数，而不是元素个数
'''
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [1] * N
    def find(self, x):
        if x != self.parents[x]:
            x = self.find(self.parents[x])
        return x
    def union(self, child, parent):
        ichild, iparent = self.find(child), self.find(parent)
        if self.size[ichild] > self.size[iparent]:
            iparent, ichild = ichild, iparent
        self.parents[ichild] = iparent
        self.size[iparent] += self.size[ichild]
 
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        N = len(nums)
        uf = UF(max(nums) + 1)
        # factors = {}
        # for n in nums:
        #     factors[n] = self.get_factors(n)
        # print(factors)
        for n in nums:
            for k in range(2, int(n ** 0.5) + 1):
                if not n % k:
                    uf.union(n, k)
                    uf.union(n, n//k)
        counts = {}
        for n in nums:
            nid = uf.find(n)
            counts[nid] = counts.get(nid, 0) + 1
        return max(counts.values())