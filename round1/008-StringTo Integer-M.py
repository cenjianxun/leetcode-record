'''
8. String to Integer (atoi)
'''

'''
忘记考虑空了
可以使用s.isdigit() # 针对s为str的情况

** str -> int 可以使用：ord(c) - ord('0 ')
'''
# faster than 21.44% of Python3
class Solution:
    def myAtoi(self, s: str) -> int:
        ss = s.strip().split(' ')[0]
        if not ss:
            return 0
        if ss[0] == '-':
            flag = -1
            slist = list(ss)[1:]
        elif ss[0] == '+':
            flag = 1 
            slist = list(ss)[1:]
        elif any(d in ss[0] for d in '0123456789'): # ss[0].isdigit()
            flag = 1
            slist = list(ss)
        else:
            return 0
        num = 0
        while slist:
            n = slist.pop(0)
            if not any(d in n for d in '0123456789'): # n.isdigit()
                break 
            num = num * 10 + int(n)
        num = num * flag
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 -1
        else:
            return num