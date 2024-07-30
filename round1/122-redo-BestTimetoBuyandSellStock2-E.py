'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

'''

def maxProfit( prices: List[int]) -> int:
    profit = 0
    for i in range(0, len(prices)-1):
        if prices[i+1] > prices[i]:
            profit = profit + prices[i+1] - prices[i]
    return profit

'''
自己做的👇
'''
def maxProfit(self, prices: List[int]) -> int:
    res = 0
    minp = maxp = prices[0]
    temp = 0
    for p in prices + [0]:
        # print(p, maxp, minp)
        if p > maxp:
            maxp = p
            temp = max(temp, maxp - minp)
        else:
            res = res + temp
            minp = maxp = p
            temp = 0
        # print(temp, res)
    return res

'''
两个区别，我记了一个最低点。它只要有增就顺着加。
按结果来看这两个效果应该是一样的
一直升：124：2-1+4-2 = 4-1
升降升：104：就是4-0
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = prices[0]
        profit = 0
        for p in prices:
            if p > sell:
                sell = p
                profit += sell - buy
            buy = sell = p
        return profit