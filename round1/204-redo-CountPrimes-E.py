'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
'''

# faster than 17.04% of Python3
def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    dp = [1] * n
    dp[0] = 0
    dp[1] = 0
    i = 0
    res = 0
    while i < n:
        if dp[i] == 1:
            res = res + 1
            j = 2
            while i * j < n:
                dp[i*j] = 0
                j = j + 1
        i = i + 1
    return res

'''
只考虑根号n之前的。然后按i往上加

'''
# faster than 60.07% of Python3
def countPrimes(self, n: int) -> int:
    if n < 2:
        return 0
    dp = [1] * n
    dp[0] = dp[1] = 0

    for i in range(2, int(n**0.5)+1):
        if dp[i] == 1:
            j = i * i
            while j  < n:
                dp[j] = 0
                j = j + i
    return sum(dp)

'''
要两个地方优化才可以：
1. 总数算i开根号的：为什么，因为一个数的质因数都是成对出现的，比如100 = 1*100 = 2*50 = …..= 10*10
2. 🟡j从i平方开始算，往上加i🟡：为什么，因为要算i的倍数，但是该倍数中，小于i的倍数在之前算这个数的时候都算过了，所以从倍数i开始算
'''