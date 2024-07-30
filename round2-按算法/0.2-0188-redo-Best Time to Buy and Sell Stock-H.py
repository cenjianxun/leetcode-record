'''
Best Time to Buy and Sell Stock
股票问题：
	121：买卖一次
	122：买卖无数次
	123：最多买卖两次
	188：最多买卖给定的k次
	309：买卖无数次，但卖完第二天不能买
	714：买卖无数次，但有交易费
'''

'''
思路：每次保证买和卖后手上钱最大，需要记录买和卖的状态

如果允许k次交易，buy和sell就各自有k个状态+1个前置状态
buy = [float('-inf')] * (k+1)
sell = [0] * (k+1)
buy初始一定是负无穷，buy表示买了当前此时最大值，但是只要买了一次，就应该取那一次，即使是负数，所以这个前置值一定比最负债的状态还要低。

每次先买后卖:
buy[i] = max(buy[i], sell[i-1] - p)
sell[i] = max(sell[i], buy[i] + p)

如果只允许一次买卖，sell[i-1]的地方就永远是sell[0] = 0
    buy, sell = -float("inf"), 0
    for p in prices:
        buy = max(buy, 0 - p)
        sell = max(sell, buy + p)

如果k无穷大，sell[i-1]的地方就永远是preSell
    buy, sell = -float("inf"), 0
    for p in prices:
        buy = max(buy, sell - p)
        sell = max(sell, buy + p)

* k的值 = min(k, len(prices)//2)，因为完成一次有收益的交易 需要两天买一天卖一天
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(k, len(prices)//2)
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i-1] - p)
                sell[i] = max(sell[i], buy[i] + p)
        return sell[-1]


'''
有一天冷静期，就需要记录再前一天的sell
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, preSell = float('-inf'), 0, 0
        for p in prices:
            buy = max(buy, preSell - p)
            preSell, sell = sell, max(sell, buy + p)
        return sell

'''
有交易费就减去fee
* 在buy or sell任一地方减一次即可
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float('-inf'), 0
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        return sell