'''
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''

def hammingWeight(n: int) -> int:
    n = str(bin(n))
    # num = 0
    # for s in n:
    #     if s == '1':
    #         num = num + 1
    # return num
    return n.count('1')

'''
有点诡异 +=可以 = + 报错
'''
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

'''
n-1 的二进制表示是n的最后一个1表示变成0，那个1表示之后的0都变成1。

那么n-1&n 就是在那个1之前的所有数都保留，那个1以及它之后的数都变成0。

1次n-1&n的操作，可将n的最后一个1变成了0，也说明这有一个1，直到n-1&n 为0的时候，我们就直到所有1的处理完毕了。
 
'''

def hammingWeight(n):
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res
