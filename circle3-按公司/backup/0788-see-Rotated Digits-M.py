'''
788. Rotated Digits

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

 
Example 1:

	Input: n = 10
	Output: 4
	Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
	Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
	Example 2:

	Input: n = 1
	Output: 0
	Example 3:

	Input: n = 2
	Output: 1

Constraints:
1 <= n <= 104
'''

'''
原来没有简便算法
'''
# faster than 33.58% of Python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(2, n+1):
            if any(d in str(i) for d in '347'):
                continue
            if any(d in str(i) for d in '2569'):
                res += 1
        return res

'''
用前面的结果
'''
# faster than 84.16% of Python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n+1)
        count = 0 
        for i in range(0, n+1):
            if i < 10:
                if i in {0, 1, 8}:
                    dp[i] = 1 
                if i in {2, 5, 6, 9}:
                    dp[i] = 2 
                    count += 1
            else:
                a, b = dp[i//10], dp[i%10] 
                if a == 1 and b == 1:
                    dp[i] = 1 
                elif a >= 1 and b >= 1:
                    dp[i] = 2 
                    count += 1
        return count 