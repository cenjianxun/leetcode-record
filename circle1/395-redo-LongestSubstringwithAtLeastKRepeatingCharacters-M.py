'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
'''

'''
不要从符合的下手，可以排除不符合的
'''

# faster than 59.76% of Python3
from collections import Counter
import re
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         dic = Counter(s)
#         not_k = [d for d in dic if dic[d] < k]
#         if not not_k:
#             return len(s)
#         ss = re.split('|'.join(not_k), s)
#         return max([self.longestSubstring(sub_s, k) for sub_s in ss])


# faster than 88.96% of Python3
# less than 94.32% of Python3
def longestSubstring(s: str, k: int) -> int:
    length = len(s)
    if length == 0 or k > length:
        return 0
    if k < 2:
        return length

    def countHandler(s: str, k: int, start: int, end: int) -> int:
        if k > end - start + 1:
            return 0
        # 初始化数组
        times = Counter(s[start:end+1])

        # 起点、终点夹逼，去掉首位不符合条件的字符串(滑动窗口)
        while end - start + 1 >= k > times[s[start]]:
            start += 1
        while end - start + 1 >= k > times[s[end]]:
            end -= 1
        print(start, end, s[start],s[end],times)
        if k > end - start + 1:
            return 0
        # 字符串中间存在不符合条件的字符，即以该字符串为界，分割前子串和后字串，进行计算(分治)
        for i in range(start, end):
            if times[s[i]] < k:
                return max(countHandler(s, k, start, i - 1), countHandler(s, k, i + 1, end))
        return end - start + 1

    return countHandler(s, k, 0, length - 1)


s = "ababacb"
k = 3
result = longestSubstring(s, k)


from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        if len(s) < k:
            return 0
        for i in set(s):
            if s.count(i) < k:
                return max(self.longestSubstring(subs,k) for subs in s.split(i))
        return len(s)