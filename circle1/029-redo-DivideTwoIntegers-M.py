'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

'''
二分法：次数等于指数
'''

def divide(dividend: int, divisor: int) -> int:
    if abs(dividend) < abs(divisor):
        return 0
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        flag = 1
    else:
        flag = -1
    dividend, divisor = abs(dividend), abs(divisor)
    times = 0
    while dividend >= divisor:
        nd = divisor
        rest_t = 1
        while dividend - nd >=0:
            nd <<=1
            rest_t <<= 1
        rest_t >>= 1
        nd >>= 1
        times = times + rest_t
        dividend = dividend - nd
    if flag == 1:
        if times > 2**31 - 1:
            return 2**31 - 1
        else:
            return times
    if flag == -1:
        if times < -2**31:
            return -2**31
        else:
            return 0 - times