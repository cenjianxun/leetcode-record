'''
319. Bulb Switcher
Medium

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Example 1:

	Input: n = 3
	Output: 1
	Explanation: At first, the three bulbs are [off, off, off].
	After the first round, the three bulbs are [on, on, on].
	After the second round, the three bulbs are [on, off, on].
	After the third round, the three bulbs are [on, off, off]. 
	So you should return 1 because there is only one bulb is on.

Example 2:

	Input: n = 0
	Output: 0

Example 3:

	Input: n = 1
	Output: 1
 
Constraints:

	0 <= n <= 109
'''

'''
翻译：因数为奇数的值的个数。
注意从1开始range
但超时
'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if self.countFactor(i)%2:
                res += 1
        return res 

    def countFactor(self, x):
        factors = {1, x}
        k = 2
        while k <= x**0.5:
            if not x%k:
                factors.add(k)
                factors.add(x//k)
            k += 1
        return len(factors)

'''
原来只有完全平方数才有奇数个因数！
但超时
'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            res += self.issquare(i)
        return res 

    def issquare(self, x):
        if int(x**0.5) **2 == x:
            return 1
        else:
            return 0
'''
无语
'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)