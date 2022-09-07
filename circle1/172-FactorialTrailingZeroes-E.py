'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

'''
天哪！不容易啊
'''

def trailingZeroes(n: int) -> int:
    result = 0
    i = 1
    num = n//(5**i)
    while num:
        result = result + num  
        i = i + 1
        num = n//(5**i)
    return int(result)