'''
792. Number of Matching Subsequences
Medium

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Example 1:

    Input: s = "abcde", words = ["a","bb","acd","ace"]
    Output: 3
    Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:

    Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    Output: 2
 
Constraints:

    1 <= s.length <= 5 * 104
    1 <= words.length <= 5000
    1 <= words[i].length <= 50
    s and words[i] consist of only lowercase English letters.
'''

'''
超时
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        count = {}
        for i, char in enumerate(s):
            if char not in count:
                count[char] = []
            count[char].append(i)
        
        print(count)
        for word in words:
            flag = 1
            index = 0
            for w in word:
                if w not in count:
                    flag = 0
                    break
                i = 0
                while i < len(count[w]) and count[w][i] < index:
                    i += 1
                if i == len(count[w]):
                    flag = 0
                    break
                index = count[w][i] + 1
                #print(w, i, count[w], index)
            res += flag
        return res

'''
find 应该是二分，比while循环快
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        chars = set(list(s))
        for word in words:
            index = -1
            flag = 1
            for w in word:
                if w not in chars:
                    flag = 0
                    break
                index = s.find(w, index + 1)
                if index == -1:
                    flag = 0
                    break
            res += flag
        return res

'''
这代码太牛逼了吧
'''    
def numMatchingSubseq(self, S: str, words: List[str]) -> int:
    waiting = defaultdict(list)
    for w in words:
        waiting[w[0]].append(iter(w[1:]))  # 存储以w[0]开头的前缀，此时waiting = {'a': [[], ['c', 'd'], ['c', 'e']], 'b': [['b']]}
    for c in S:
        for it in waiting.pop(c, ()):
            waiting[next(it, None)].append(it)  # 在本题的例子中 it 分别为[]、['c', 'd']、['c', 'e']
    return len(waiting[None])



 

 