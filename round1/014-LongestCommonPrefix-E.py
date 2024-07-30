
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

# faster than 98.38% of Python3
def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    
    def compair(s1, s2):
        i = len(s1) 
        while i > 0:
            if s2.startswith(s1[0:i]):
                break
            else:
                i = i - 1
        return s1[0:i]
    
    s = compair(strs[0], strs[1])
    for i in range(2, len(strs)):
        s = compair(s, strs[i])
    return s