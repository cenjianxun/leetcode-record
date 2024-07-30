'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
'''


def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        return 0
    # return haystack.find(needle)
    i = 0

    flag = -1
    while i < len(haystack):
        if haystack[i] == needle[0]:
            flag = i
            if len(haystack) - i >= len(needle) and haystack[i:i+len(needle)] == needle:
                return flag
            else:
                flag = -1
                i = i + 1
        else:
            i = i + 1
    return flag