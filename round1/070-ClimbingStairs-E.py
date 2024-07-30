'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

'''
递归会超时
有6种解法！！！！！！！！！
'''


def climbStairs(n: int) -> int:
    # if n < 3:
    #     return n
    # if n > 2:
    #     nums = climbStairs(n-1) + climbStairs(n-2)
    #     print(n, nums)
    #     return nums

    nums = [1] * n
    if n > 1:
        nums[1] = 2
    for i in range(2, n):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[-1]

r = climbStairs(30)
print(r)
'''
这个题需要重看的原因就是直接递归会超时
->动态规划
->只用一个temp存。（必须同时赋值
'''

# faster than 78.92% of Python3
def climbStairs(n: int) -> int:
    pre, cur = 1, 1
    for i in range(1, n):
        pre, cur = cur, cur + pre
    return cur