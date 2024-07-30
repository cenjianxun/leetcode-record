'''
121. Best Time to Buy and Sell Stock

you are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''


def maxProfit(prices) -> int:
    profit = 0
    buy = prices[0]
    for p in prices:
        if p < buy:
            buy = p
        profit = max(profit, p-buy)
    return profit

'''
自己做的！👇
'''
def maxProfit(prices) -> int:
    stack = []
    res = 0
    for n in prices:
        while stack and stack[-1] > n:
            m = stack.pop()
            if stack:
                res = max(res, m - stack[0])
        stack.append(n)
    if stack:
        res = max(res, stack[-1] - stack[0])
    return res

def maxProfit(self, prices: List[int]) -> int:
    minp = maxp = prices[0]
    res = 0
    for n in prices:
        if n > maxp:
            maxp = n
            res = max(res, maxp - minp)
        if n < minp:
            minp = maxp = n
    return res

'''
一个搓方法
'''
def maxProfit(self, prices: List[int]) -> int:
    
    while prices:
        tail = prices[-1]
        if len(prices) > 1 and tail <= prices[-2]:
            prices.pop()
        else:
            break
    if len(prices) < 2:
        return 0
    while prices:
        head = prices[0]
        if len(prices) > 1 and head >= prices[1]:
            prices = prices[1:]
        else:
            break
    min1 = min(prices)
    max2 = max(prices)
    index = prices.index(min1)
    max1 = max(prices[index:])
    
    index = prices.index(max2)
    min2 = min(prices[:index+1])
    return max(max(max1-min1, 0), max(max2-min2, 0))


'''
总之就是单调栈
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for p in prices:
            while stack and stack[-1] > p:
                stack.pop()
            if stack:
                profit = max(profit, p - stack[0])
            stack.append(p)
        return profit