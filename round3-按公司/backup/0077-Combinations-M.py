'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:

	Input: n = 4, k = 2
	Output:
	[
	  [2,4],
	  [3,4],
	  [2,3],
	  [1,2],
	  [1,3],
	  [1,4],
	]

Example 2:

	Input: n = 1, k = 1
	Output: [[1]]
 
Constraints:

	1 <= n <= 20
	1 <= k <= n
'''

# faster than 5.01% of Python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ranges = [[i] for i in range(1, n+1)]
        if k == 1:
            return ranges
        i = 2
 
        while i <= k:
            stack = []
            for r in ranges:
                #print(r)
                for c in range(r[-1]+1, n+1):
                    stack.append(r + [c])
            ranges = stack
            i += 1
        return ranges

'''
回溯
'''
    def combine(self, n, k):   
            sol=[]
            def backtrack(remain,comb,nex):
                # solution found
                if remain==0:
                    sol.append(comb.copy())
                else:
                    # iterate through all possible candidates
                    for i in range(nex,n+1):
                        # add candidate
                        comb.append(i)
                        #backtrack
                        backtrack(remain-1,comb,i+1)
                        # remove candidate
                        comb.pop()

            backtrack(k,[],1)
            return sol