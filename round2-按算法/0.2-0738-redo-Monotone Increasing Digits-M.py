'''
738. Monotone Increasing Digits
Medium

An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

Example 1:

	Input: n = 10
	Output: 9

Example 2:

	Input: n = 1234
	Output: 1234

Example 3:

	Input: n = 332
	Output: 299
 
Constraints:

	0 <= n <= 109
'''

'''
1. 倒着算
2. 如果碰上小的，后面所有位都要为9

ep: 332, 100
'''
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nlist = list(str(n))
        i = len(nlist) - 2
        while i >= 0:
            if nlist[i] > nlist[i+1]:
                nlist[i] = str(int(nlist[i]) - 1)
                nlist[i+1:] = '9' * (len(nlist) - i - 1)
            i -= 1
            print(i, nlist)
        return int(''.join(nlist))