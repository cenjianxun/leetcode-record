'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''


def plusOne(self, digits):
    n = 0
    for e in digits:
        n = n * 10 + e
    n = n + 1
    return [int(i) for i in list(str(n))]