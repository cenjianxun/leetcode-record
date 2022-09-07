'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''

'''
1、折半查找
2、折半是头尾/2,而不是自身平方或者/2

** mid的选择有讲究，是选head还是tail。
一个解释：因为int是向下取整，所以mid需要选tail
'''


def mySqrt(x: int) -> int:
    head = 0 
    tail = x
    mid = x
    while head <= tail:
        if mid * mid <= x and (mid+1) * (mid+1) > x:
            return mid
        if mid * mid > x:
            tail = mid
            mid =  (head + tail)//2 
        elif (mid+1) * (mid+1) <= x:
            head = mid 
            mid = (head + tail)//2 