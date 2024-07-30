'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
典型递归，dfs，需要敏感性这种。
本题关键词：所有可能种类
'''
# faster than 72.16% of Python3
def combinationSum(cands: List[int], target: int) -> List[List[int]]:
    res = []
    cands.sort(reverse=True)
    print(cands)
    def helper(temp, i, rest):
        # print(i,  temp, rest)
        if rest == 0:
            temp.sort()
            if not temp in res:
                res.append(temp)
            return  
        if rest < cands[-1]:
            return 
        for j in range(i, len(cands)): 
            helper(temp + [cands[j]], j, rest - cands[j])
    
    temp = []
    rest = target
    helper(temp, 0, rest)

    res.sort()
    return res


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    #candidates.sort()
    def dfs(start, comb):
        if sum(comb) >= target:
            if sum(comb) == target:
                res.append(comb)
            return
        for i in range(start, len(candidates)):
            dfs(i, comb + [candidates[i]])
    dfs(0, [])
    return res