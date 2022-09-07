'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

'''
还可以先排序再比较
'''
def isAnagram(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    i = 0
    while i < len(s):
        print(s[i], t[i])
        if s.count(s[i]) != t.count(s[i]):
            return False
        i = i + 1
    return True