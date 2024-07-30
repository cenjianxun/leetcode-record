'''
Write a function that reverses a string. The input string is given as an array of characters s.
'''

'''
还有更快的  faster than 36.34% of Python3
'''
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    while i < len(s)-1-i:
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        i = i + 1