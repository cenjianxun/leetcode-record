'''
686. Repeated String Match
Medium

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:

	Input: a = "abcd", b = "cdabcdab"
	Output: 3
	Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:

	Input: a = "a", b = "aa"
	Output: 2
 
Constraints:

	1 <= a.length, b.length <= 104
	a and b consist of lowercase English letters.
'''

'''
1.如果b里面有a没有的char，return -1，否则进入2
2.前提：b的长度是a的x倍，则只有三种情况，重复x次、x+1次、x+2次，否则不包含。
  这是因为：
  下限是x次，因为是a的x倍，所以最少重复x次，这时是完全重合
  上限是x+2次，开头额外匹配一部分，结尾额外匹配一部分


另：KMP算法：解决子串匹配问题
https://leetcode.cn/problems/repeated-substring-pattern/solution/acm-xuan-shou-tu-jie-leetcode-zhong-fu-d-vl7i/
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        for i in range(1, len(b)//len(a) + 3):
            if b in a * i:
                return i
        return -1