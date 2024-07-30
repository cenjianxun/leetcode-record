'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
这个动态规划的精髓是，只有当dp[i]为真的话，s[i:~~~]以i开头的才往下判断
dp的i和s的i错了一位
'''

def wordBreak(s: str, wordDict: List[str]) -> bool:
    n, dp = len(s), [True] + [False]*len(s)
    for i in range(n):
        for j in range(i+1):
            # print(j, i + 1, s[j:i+1])
            if dp[j] and s[j:i+1] in wordDict:
                dp[i+1] = True
                # print(j, i + 1, s[j:i+1], dp)
                break
    return dp[n]



'''
超时
'''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordmap = defaultdict(set)
        for word in wordDict:
            wordmap[word[0]].add(word)
        #print(wordmap)
        res = False
        def helper(s, res):
            if not s:
                return True
            for word in wordmap[s[0]]:
                if word == s[:len(word)]:
                    res = helper(s[len(word):], res)
            return res
                    
        return  helper(s, res)

'''
dp
'''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [1] + [0] * len(s)
        start = 0
        for i in range(len(s)):
            if dp[i]:
                for word in wordDict:
                    print(i, word, s[i:i+len(word)], dp)
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = 1
        return dp[-1]