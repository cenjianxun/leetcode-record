'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        slist = list(s)[::-1]
        while slist:
            i = slist.pop()
            if slist:
                j = slist.pop()
                if r_to_d[i] >= r_to_d[j]:
                    num = num + r_to_d[i]
                    slist.append(j)
                else:
                    num = num + r_to_d[j] - r_to_d[i]
            else:
                num = num + r_to_d[i]
        return num