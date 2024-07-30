'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

'''
竟然直接2**31 无语

** python 不会主动溢出
'''

class Solution:
    def reverse(self, x):
        if x == 0 :
            return 0
        if x > 0:
            flag = 1
        if x < 0:
            flag = -1
            x = -1 * x
        rest = x
        num = 0

        while rest:
            num = num * 10 + rest % 10  
            rest = rest//10
        num = flag * num
        if num > 2**31 -1 or num < -2**31:
            return 0
        else:
            return num