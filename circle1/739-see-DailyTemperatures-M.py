'''
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

'''
没做出来
* 参数范围也是一个提醒
温度范围比较小，所以遍历温度
* 遍历温度也不一定要按index创建[]

思想巧妙的点：
遍历的当下i时，并非赋值res[i], 而是把i当成tail，依次赋值i之前的res[j]
刚好最后一个值不用管，只当边界
T[i]存的是i-1，以及再之前降序的值，那么i就是比stack里的大的最近的那个值
'''

# faster than 76.19% of Python3
def dailyTemperatures(self, T: List[int]) -> List[int]:
    wait = [0]*len(T)
    stack = []
    
    for i, x in enumerate(T):      
        while stack and x > T[stack[-1]]:
            j = stack.pop()
            wait[j] = i - j
        stack.append(i)
    
    return wait

'''
1027
做出了
'''
def dailyTemperatures(self, T: List[int]) -> List[int]:
    n = len(T)
    stack, res = [], [0] * n
    for i in range(n - 1, -1, -1):
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res