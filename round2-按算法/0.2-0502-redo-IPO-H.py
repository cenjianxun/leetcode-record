'''
502. IPO
Hard

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

	Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
	Output: 4
	Explanation: Since your initial capital is 0, you can only start the project indexed 0.
	After finishing it you will obtain profit 1 and your capital becomes 1.
	With capital 1, you can either start the project indexed 1 or the project indexed 2.
	Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
	Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Example 2:

	Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
	Output: 6
 
Constraints:

	1 <= k <= 105
	0 <= w <= 109
	n == profits.length
	n == capital.length
	1 <= n <= 105
	0 <= profits[i] <= 104
	0 <= capital[i] <= 109
'''

'''
超时
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_map = {} 
        for i, c in enumerate(capital):
            if not c in capital_map:
                capital_map[c] = []
            capital_map[c].append(i)
        
        final = w
        #print(capital_map)
        while k > 0:
            max_profit = [0, -1]
            for c in range(final + 1):
                if c in capital_map:
                    for i in capital_map[c]:
                        if profits[i] > max_profit[0]:
                            max_profit = [profits[i], i]
                            flag = 1
            profits[max_profit[1]] = 0
            final += max_profit[0]
            k -= 1
            #print(k, max_profit, final)
        return final

'''
增加了一个如果w大于所有profit,就直接取前k个
'''           
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        k = min(len(profits), k)
        if w < max(capital):
            while k > 0:
                max_profit = [-1, -1]
                for i in range(len(profits)):
                    if w >= capital[i] and profits[i] > max_profit[0]:
                        max_profit = [profits[i], i]
                if max_profit[1] == -1:
                    break
                w += max_profit[0]
                capital[max_profit[1]] = float('inf')
                k -= 1
        else:
            profits.sort(reverse=True)
            w += sum(profits[:k])
        return w