'''
424. Longest Repeating Character Replacement
Medium

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

	Input: s = "ABAB", k = 2
	Output: 4
	Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

	Input: s = "AABABBA", k = 1
	Output: 4
	Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
	The substring "BBBB" has the longest repeating letters, which is 4.
 
Constraints:

	1 <= s.length <= 105
	s consists of only uppercase English letters.
	0 <= k <= s.length
	Accepted
	254,177
	Submissions
	497,427
'''

'''
遍历每一个存在的字母
右，一直前进，直到囊括所有的非指定字母。在这个过程中每一轮都比较res，因为尚未达到目标且逐步接近，所以一定res每轮都不超出条件限制。（当count刚好=k时其实是最大res，这时也比较了。）
一旦超过k，立刻缩左边，同时-count，直到不达到条件，完成这些才再次比较res，所以所有的res都满足条件
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        existed = set(list(s))
        for c in existed:
            l = r = count = 0
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res

'''
另一个解法：用map存储，维护最大，
注意这个解法判断超出的条件：if r - l + 1 - longest > k
* 因为当前map里的长度一定在滑动窗口内，所以这个在滑动窗口内的longest+需要改变的k个字符就是当前窗口的长度
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        longest = 0
        count = defaultdict(int)
        l = r = 0
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            longest = max(longest, count[ord(s[r]) - ord('A')])
            print(l, r, longest, count)
            if r - l + 1 - longest > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
            
        return r - l