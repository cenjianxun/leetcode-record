'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

'''
动态规划的一个关键点，选择dp。
dp为每个状态的记录。本题里面选择的是amount不同值的状态。
so动态规划需要从小到大。因为后面大的运算需要用到前面小的的结果

而外层的也是从小到大，对每列来讲，取的值就是该列的min
'''

def coinChange(coins: List[int], amount: int) -> int:
    dp = [0] + [float('inf')] * amount
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]


'''
220618
bfs内存溢出
'''
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(amount, 0)])
        visited = {amount}
        while queue:
            rest, num = queue.popleft()
            if not rest:
                return num
            for c in coins[::-1]:
                if rest - c >= 0: #and not rest-c in visited:
                    queue.append((rest-c, num+1))
                    #visited.add(rest)
            #print(queue)
        return -1

'''
动态规划规划的是算出从0到amount的钱数需要用的个数，后面的依赖前面的
'''