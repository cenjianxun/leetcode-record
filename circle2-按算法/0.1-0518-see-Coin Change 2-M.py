'''
518. Coin Change 2
Medium

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

    Input: amount = 10, coins = [10]
    Output: 1
 
Constraints:

    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                if i < c:
                    continue
                dp[i] += dp[i-c]
        return dp[-1]

'''
i 是coins的index
排列的意思是对target来说，它为（coin里每一个c的所有组合的个数）之和
f[i][j] = f[i][j-c[0]] + f[i][j-c[1]] +...+ f[i][j-c[i]] ①
①中，每一项表示在f[i][j-c[k]]基础上加上c[k]达成金额j的组合数，也即由前i个coin组成金额j且至少存在一个coin[k]的组合数。
一共i项，每一项组合情况相互可能会有重叠的情况。

例如有硬币{1,2}组成5，f[1][5] = f[1][3] + f[1][4].
  f[1][3]中有{1,1,1},{1,2} 再加入{2}.即 {1,1,1,2}{1,2,2}
  f[1][4]中有{1,1,1,1}{1,1,2}{2,2} 再加入{1}。{1,1,1,1,1}{1,1,2,1}{2,2,1} 
实际上，其中{1,1,1,2}与{1,1,2,1}、{1,2,2}与{2,2,1}是同一种组合情况，重复进行了计数，结果是5


正确情况应该为：
组合的意思是对target来说，它为包含当前coin且钱数差coin的个数 和 差当前coin且钱数已经为target的个数 之和
f[i][j] =f[i-1][j] + f[i][j-c[i]];
f[i-1][j] = f[i-2][j] + f[i-1][j-c[i-1]]
...
f[1][j] = f[0][j] + f[1][j-c[1]]
f[0][j] = f[0][j-c[0]]
上式两边相加得

f[i][j] = f[0][j-c[0]] + f[1][j-c[1]] +...+ f[i][j-c[i]] ②
②中，每一项表示在f[k][j-c[k]]基础上加上c[k]达成金额j的组合数，也即由前k个coin组成金额j且至少存在一个coin[k]的组合数。不重不漏地将f[i][j]分成i组。

例如有硬币{1,2}组成5，f[1][5] = f[0][4] + f[1][3].
  f[0][4]中有{1,1,1,1} + {1}. 即{1,1,1,1,1}
  f[1][3]中有{1,1,1}{1,2} + {2}。{1,1,1,2}{1,2,2}
所有组合情况加起来不重不漏，结果为3


5
[1,2,5]

i:1, c:1, dp[1] += dp[1-1] = 1 1:dp[0]
i:2, c:1, dp[2] += dp[2-1] = 1 2:dp[1] 
i:3, c:1, dp[3] += dp[3-1] = 1 3:dp[2] = dp[1]
i:4, c:1, dp[4] += dp[4-1] = 1 4:dp[3] = dp[1]
i:5, c:1, dp[5] += dp[5-1] = 1 5:dp[4] = dp[1]
i:2, c:2, dp[2] += dp[2-2] = 2 2:dp[1],dp[0] = dp[2],dp[1]
i:3, c:2, dp[3] += dp[3-2] = 2 3:dp[2],dp[1] = dp[2],dp[1]
i:4, c:2, dp[4] += dp[4-2] = 3 4:dp[3],dp[2] = dp[2],dp[1]
i:5, c:2, dp[5] += dp[5-2] = 3 5:dp[4],dp[3] = dp[2],dp[1]
i:5, c:5, dp[5] += dp[5-5] = 4 5:dp[4],dp[3],dp[0] = dp[2],dp[1],dp[5]

i:1, c:1, dp[1] += dp[1-1] = 1 1:dp[0]
i:2, c:1, dp[2] += dp[2-1] = 1 2:dp[1]
i:2, c:2, dp[2] += dp[2-2] = 2 2:dp[1],dp[0]
i:3, c:1, dp[3] += dp[3-1] = 2 3:dp[2]
i:3, c:2, dp[3] += dp[3-2] = 3 3:dp[2],dp[1]
i:4, c:1, dp[4] += dp[4-1] = 3 4:dp[3],
i:4, c:2, dp[4] += dp[4-2] = 5 4:dp[3],dp[2]
i:5, c:1, dp[5] += dp[5-1] = 5 5:dp[4]
i:5, c:2, dp[5] += dp[5-2] = 8 5:dp[4],dp[3]
i:5, c:5, dp[5] += dp[5-5] = 9 6:dp[4],dp[3],dp[0]
'''