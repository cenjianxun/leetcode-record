'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

def countBits(self, n: int) -> List[int]:
    res = []
    for i in range(n + 1):
        c = 0
        b = i
        while b:
            if b & 1:
                c = c + 1
            b = b >> 1
        res.append(c)
    return res

'''
see时间复杂度为O(n)的方法：
下一个的值是之前所有值+1
res[i>>1] 是除去个位的值的1的个数
i&1 是i的个位的1个数 （1 or 0）
❗ res[] + i&1 ❌
    res[] + (i&1) ✔
❗ 位运算优先级低于算数符号
'''

def countBits(self, n: int) -> List[int]:
    res = [0]
    for i in range(1, n + 1):
        # print(i, i>>1, res[i>>1], i &1)
        res.append(res[i>>1] + (i & 1))
    return res 