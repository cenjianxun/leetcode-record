'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

'''
1是的
'''
# faster than 64.80% of Python3
def isPowerOfThree(n: int) -> bool:
    d = 3
    # rest = n
    res = 1
    if n == 1:
        return True
    if not n%2:
        return False
    while res * d < n:
        while res * d * d < n:
            d = d * d
        print(res, d)
        if res * d * d == n:
            return True
        if res * d * 3 > n:
            return False
        elif res * d * 3 == n:
            return True
        else:
            res = res * d 
            d = 3
    if res * d == n:
        return True
    else:
        return False

# ↑↑↑↑↑↑↑↑↑↑↑ 不能用循环！↑↑↑↑↑↑↑↑↑↑↑↑


def isPowerOfThree(n):
    '''
    它的log值再幂如果还是n 就说明是
    '''
    return False if n <= 0 else n == pow(3, round(math.log(n, 3)))

    '''
    在范围内最大是power(3, 19)
    需要大于0
    '''
    return n > 0 and 1162261467 % n == 0
    return False if n<=0 or pow(3, 19)%n else True