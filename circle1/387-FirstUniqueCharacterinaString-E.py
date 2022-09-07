'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
'''

'''
def firstUniqChar(s: str) -> int:
'''
    # faster than 20.90% of Python3， 
    # less than 44.25% of Python3
    dic = {}
    for i in range(0, len(s)):
        if not s[i] in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] = dic[s[i]] + 1
把这段换成Counter 速度变成66.47%
'''
    # faster than 66.47% of Python3
    # less than 70.02% of Python3
    # 计数的基数从s本身变成标准字母，可用find，count，index等函数
    from collections import Counter
    dic = Counter(s)
    i = 0
    while i < len(s):
        if dic[s[i]] == 1:
            break
        i = i + 1
    if i == len(s):
        return -1
    else:
        return i 

# faster than 99.52% of Python3
# less than 87.99% of Python3
def firstUniqChar(s: str) -> int:
    return min([s.find(c) for c in 'abcdefghijklmnopqrstuvwxyz' if s.count(c) == 1] or [-1]) 