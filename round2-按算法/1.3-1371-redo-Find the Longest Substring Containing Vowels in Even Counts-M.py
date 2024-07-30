'''
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:

	Input: s = "eleetminicoworoep"
	Output: 13
	Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:

	Input: s = "leetcodeisgreat"
	Output: 5
	Explanation: The longest substring is "leetc" which contains two e's.

Example 3:

	Input: s = "bcbcbc"
	Output: 6
	Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 
Constraints:

	1 <= s.length <= 5 x 10^5
	s contains only lowercase English letters.
'''

'''
不过 要用bits
'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        preCount = {'a':0, 'e':0, 'o':0, 'i':0, 'u':0}
        preIndex = {'a':{0:-1}, 'e':{0:-1}, 'i':{0:-1}, 'o':{0:-1}, 'u':{0:-1}}
        for i, c in enumerate(s):
            if c in preCount:
                preCount[c] = (preCount[c] + 1)%2
                if preCount[c] not in preIndex[c]:
                    preIndex[c][preCount[c]] = i
            dis = float('inf')
            for k, v in preCount.items():
                dis = min(dis, i - preIndex[k][v])
            res = max(res, dis)
        return res

'''
1代表奇0代表偶，有几个值需要判断就有几位 这里5位
是哪个值就挪到相应位数。
增加奇偶用异或 1<<相应位数，再异或，就表示当前这位的数的奇偶的个数

存储长度是总状态的个数 就是2 ** 位数
dp[0]要置-1，表示开始之前 index=-1时，5个数都没有偶数
'''
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        dp = [float('-inf')] * (2**5)
        dp[0] = -1
        pattern = 0
        bits = {'a':4,'e':3,'i':2,'o':1,'u':0}
        for i, c in enumerate(s):
            if c in bits:
                pattern = pattern ^ (1<<bits[c])
            if dp[pattern] != float('-inf'):
                res = max(res, i - dp[pattern])
            else:
                dp[pattern] = i
        print(dp)
        return res