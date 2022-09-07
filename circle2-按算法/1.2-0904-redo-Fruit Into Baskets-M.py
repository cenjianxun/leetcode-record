'''
904. Fruit Into Baskets
Medium

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:

    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.

Example 2:

    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].
    If we had started at the first tree, we would only pick from trees [1,2].
 
Constraints:

    1 <= fruits.length <= 105
    0 <= fruits[i] < fruits.length
'''

'''
超时
改成left = right - 1
因为：
blocks = [1, _2_, 1, 2, 1, 2, _1_, 3, ...] 
当考虑3时，不需要从第二个元素2（也就是标记成 _2_ 的数字）开始考虑，只用从 3 之前的第一个元素开始考虑（_1_）。
因为如果从前两个或更多元素开始，这个序列一定包含类型 1 和 2，所以序列一定会在 3 处停止，这就比已经考虑的序列更短了。

'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = []
        left = 0
        while left < len(fruits):
            right = left
            while right < len(fruits) and fruits[left] == fruits[right]:
                right += 1
            baskets.append((fruits[left], right - left))
            left = right
        res = 0
        left = 0
        #print(baskets)
        while left < len(baskets):
            right = left + 2
            while right < len(baskets) and baskets[right][0] == baskets[right-2][0]:
                right = right + 1
            num = 0
            for i in range(left, min(len(baskets), right)):
                num += baskets[i][1]
            #print(left, right, num)
            res = max(res, num)

            # 超时：left += 1
            # 改成：
            left = right - 1
        return res

'''
for else用法：
for 里面如果有break，就不执行else
如果循环完了, 或者有continue，就执行else
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = []
        left = 0
        while left < len(fruits):
            right = left
            while right < len(fruits) and fruits[left] == fruits[right]:
                right += 1
            baskets.append((fruits[left], right - left))
            left = right
        res = 0
        i = 0
        #print(baskets)
        while i < len(baskets):
            num, types = 0, set()
            for j in range(i, len(baskets)):
                types.add(baskets[j][0])
                if len(types) >= 3:
                    i = j - 1
                    break
                num = num + baskets[j][1]
                res = max(res, num)
            else:
                break
                     
        return res

'''
又是因为每一轮（合法时）都算最大，一旦超了立刻缩左边，所以可行
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        baskets = defaultdict(int)
        i = j = res = types = 0
        while j < len(fruits):
            if baskets[fruits[j]] == 0:
                types += 1
            baskets[fruits[j]] += 1
            while types > 2:
                baskets[fruits[i]] -= 1
                if baskets[fruits[i]] == 0:
                    types -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1 
        return res