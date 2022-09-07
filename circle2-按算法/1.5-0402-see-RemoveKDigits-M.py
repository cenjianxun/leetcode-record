'''
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
'''
'''
正常解法是升序之后，额外一次处理最后一个元素，使得k还没为0的情况
'''

def removeKdigits(self, num: str, k: int) -> str:
    stack, i, n = [], 0, len(num) 
    print(n)
    while k or i < n:     
        # print(i, k, stack)
        if i < n:
            s = int(num[i])
        while stack and k and (i < n and s < stack[-1]  or k > n-i):
            stack.pop()
            k -= 1
            # print(s, num[i:], k, stack)
        if i < n:
            stack.append(s)
        # print(  stack )
        i += 1
    return str(int(''.join([str(s) for s in stack]))) if stack else '0'

'''
选最小数的思路是：使高位的值尽量小 + 如果是完全升序的值，就删除最后k个

坑比较多：
1. 最高位为0时怎么办
2. 如果空了要返回'0'
3. 循环完了k还没用完，就删最后k个
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        res = ''.join(stack).lstrip('0')
        return res if res else '0'