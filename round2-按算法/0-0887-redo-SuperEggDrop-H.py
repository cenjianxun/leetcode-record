'''
887. Super Egg Drop

You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.
'''

# https://charlesliuyx.github.io/2018/10/11/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91Egg%20Puzzle%20%E9%B8%A1%E8%9B%8B%E9%9A%BE%E9%A2%98/
'''
dp也可以是一个函数，不一定是一个数组
什么时候是一个函数？它的值需要计算的时候，分很多情况的时候

当有两个鸡蛋时，为什么不是居中取50，因为
当第一个碎了，move为50
第一个没碎，move为27
则答案为50，但是27和50之间一定有更优的值，即第一个鸡蛋选择的楼层，使得dp[第一个没碎]比27大同时dp[第一个碎]比50更小，从而使答案比50更小
需要动态找出这个值 

在每一轮中，需要遍历从1到n+1楼层
'''

# maximum recursion depth exceeded
def superEggDrop(self, k: int, n: int) -> int:
    mem = {}
    def dp(h, m):
        if m == 1:
            return h
        if h == 0:
            return 0

        if (h, m) in mem:
            return mem[(h, m)]
        res = h
        for i in range(1, n + 1):
            res = min(res, max(dp(i - 1, m - 1), dp(n - i, m)) + 1)
        mem[(h, m)] = res
        return res
    return dp(n, k)


''' 
dp表示最多能判断的楼层高
这时i不是层高，而是被允许最多投掷次数
'''
def superEggDrop(self, k: int, n: int) -> int:
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
            if dp[i][j] >=n:
                return i