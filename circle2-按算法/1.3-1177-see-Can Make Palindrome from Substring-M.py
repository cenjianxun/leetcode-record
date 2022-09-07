'''
1177. Can Make Palindrome from Substring
Medium

You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return a boolean array answer where answer[i] is the result of the ith query queries[i].

Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.

Example :

	Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
	Output: [true,false,false,true,true]
	Explanation:
	queries[0]: substring = "d", is palidrome.
	queries[1]: substring = "bc", is not palidrome.
	queries[2]: substring = "abcd", is not palidrome after replacing only 1 character.
	queries[3]: substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
	queries[4]: substring = "abcda", could be changed to "abcba" which is palidrome.

Example 2:

	Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
	Output: [false,true]
 
Constraints:

	1 <= s.length, queries.length <= 105
	0 <= lefti <= righti < s.length
	0 <= ki <= s.length
	s consists of lowercase English letters.
'''

'''
二维map
true == (该字串中出现次数为奇数的字母个数-（字串长度为奇数：1？0）)/2 <= k
注意细节
'''
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        preFre = {}
        preFre[0] = {s[0]:1}
        for i in range(1, len(s)):
            preFre[i] = preFre[i-1].copy()
            if s[i] in preFre[i]:
                preFre[i][s[i]] += 1
            else:
                preFre[i][s[i]] = 1
                
        for left, right, k in queries:
            odd = 0
            for char, fre in preFre[right].items():
                if left:
                    fre = fre - preFre[left-1].get(char, 0)
                odd += fre%2
            #print(left, right,odd,k,preFre[right])
            res.append((odd - odd%2)//2<=k)
        return res

'''
位运算：
1. 是要知道前i个数的奇数的个数。因为只有奇-偶or反过来=奇，奇-奇/偶-偶 = 偶，所以用list统计前i个的奇数个数
2. 位表示1为奇0为偶，所以差可以用异或
3. 最后奇数的个数的表示，要统计1的个数
'''
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        preCount = [0] 
        for i in range(len(s)):
            preCount.append(preCount[-1] ^ (1<<(ord(s[i]) - ord('a'))))
                
        for left, right, k in queries:
            odd = bin(preCount[right+1] ^ preCount[left]).count('1')
            #print(odd)
            res.append((odd - odd%2)//2 <=k)
        return res