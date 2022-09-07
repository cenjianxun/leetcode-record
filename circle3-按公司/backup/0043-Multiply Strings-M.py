'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

	Input: num1 = "2", num2 = "3"
	Output: "6"
	Example 2:

	Input: num1 = "123", num2 = "456"
	Output: "56088"
 
Constraints:

	1 <= num1.length, num2.length <= 200
	num1 and num2 consist of digits only.
	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        def mul_singal(num, n):
            res = 0
            n = ord(n) - ord('0')
            num = list(num)[::-1]
            for i in range(len(num)):
                cur = ord(num[i]) - ord('0')
                res = res + cur * n * (10 ** i)
            return res
        num = list(num1)[::-1]
        for i in range(len(num)):
            res = res + mul_singal(num2, num[i]) * (10 ** i)
        return str(res)