'''
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

'''

 
#超时
def numSquares(self, n: int) -> int:
    if not n:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        j = 1
        while j ** 2 <= i:
            dp[i] = min(dp[i], dp[i - j **2] + 1)
            j = j + 1
    return dp[n]


'''
四平方和定理
任何数都可以表示为<=4个数的平方和
1. 简化数字：一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同
2. 定理：如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
3. 先开方（要int）再平方等于原值，则为1
4. 分开两边，减一个完全平方数，剩下的做3，则为2
5. 剩下的为3
'''
def numSquares(self, n: int) -> int:
    while n%4 == 0:
        n = n // 4
    
    if int(n ** 0.5) ** 2 == n:
        return 1
    if n % 8 == 7:
        return 4
    i = 1
    while i ** 2 < n:
        rest = n - i ** 2
        if int(rest ** 0.5) ** 2 == rest:
            return 2
        i = i + 1
    return 3

'''
广度遍历：
需要一个queue，左出右进
需要记录层数，层数就是步数
需要一个set记录遍历过的数据，差为0则路径停止=被减数在visited里
'''
    def numSquares(self, n: int) -> int:
        base = [i*i for i in range(int(n**0.5), 0, -1)]
        print(base)
        queue = deque([(n, 1)])
        visited = {n}
        while queue:
            num, layer = queue.popleft()
            if num in base:
                return layer
            for i in base:
                if num - i > 0 and not (num-i) in visited:
                    visited.add(num-i)
                    queue.append((num-i, layer+1))
            print(num, layer, queue, visited)


'''
dfs
需要注意的地方：每一层的起始值选择：min(上一轮的值，当前余数开方)
需要减枝的地方：及时比较赋值给最小，如果当前个数已经大于全局最小就不用继续循环这一整轮
'''
    def numSquares(self, n: int) -> int:
        self.res = float('inf')
        
        def helper(n, stack, k):
            #print(n, stack, self.res)
            if not n:
                self.res = min(self.res, len(stack))
                return  
            k = min(int(n**0.5), k)
            for i in range(k, 0, -1):
                if len(stack) >= self.res:
                    continue
                helper(n-i*i, stack + [i*i], i)
     

        for i in range(int(n**0.5), 0, -1):
            print(i)
            helper(n-i*i, [i*i], i)
        return self.res

'''
dp
背包
dp[j]由dp[j - i**2]推出，加上1便是dp[j]
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]  
        for i in range(2, n+1):
            for j in range(1, int(i**0.5) + 1):
                k = i - j * j
                dp[i] = min(dp[i], dp[k]+1)
        return dp[n]
