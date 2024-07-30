'''
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

	Input: piles = [3,6,7,11], h = 8
	Output: 4
	Example 2:

	Input: piles = [30,11,23,4,20], h = 5
	Output: 30
	Example 3:

	Input: piles = [30,11,23,4,20], h = 6
	Output: 23

Constraints:

	1 <= piles.length <= 104
	piles.length <= h <= 109
	1 <= piles[i] <= 109
'''

'''
不会

二分法
本题乍看之下完全没有头绪，看了dong佬的解释才能理解。这本质上还是一个二分搜索，但是是稍微有变化的二分搜索。按照dong佬的框架，可以分为二分搜索的题目，一定有几个特征：

能建立一个自变量x

自变量x有一个单调（递增或递减）函数f(x)

能找到一个需要的target，作为约束条件f(x) == target

题目需要你找满足该约束条件时的x值

具体到本题，自变量x是koko吃香蕉的速度，f(x)是特定速度下吃完piles里面所有香蕉所需的时间hrs，target就是守卫回来的时间h（题设给出），而题目要求的是在f(x)==target的情况下，最小的x是什么。从实现上看，我们需要一个f(x, piles)来求特定速度下吃完香蕉所需的时间hrs，然后用这个hrs去判断是否大于/等于/小于h。根据和h的关系调整吃香蕉的速度。本题主要是要求到左边界，因为是要求满足h的情况下最小的那个速度值。此类题型最好画一下f(x)的曲线，明确一下单调性，这样代码也好根据要求调整。 
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + ((right - left) >> 1)
            if sum(pile // mid + (not not pile % mid) for pile in piles) > h:
                left = mid + 1
            else:
                right = mid
        return left