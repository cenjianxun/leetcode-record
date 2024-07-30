'''
Given a string s, find the length of the longest substring without repeating characters.
'''

'''
这道题看起来不难但是小细节很碎，没有想好就写结果错了三次。
好方法哎
'''

def lengthOfLongestSubstring(s):   
    if not s:                     # 如 
        return 0                  
    word = ''                      
    cur_word = ''                  
    for ss in s:                  
        if not ss in cur_word:     
            cur_word = cur_word + ss  
        else:                      
            cur_word = cur_word.split(ss)[1] + ss  
        if len(cur_word) > len(word):
            word = cur_word
        print(ss, cur_word, word)
    return len(word)   

s = lengthOfLongestSubstring("kew")
print(s)


'''
这个set的目的只是为了存重复的，不计位置也可以
'''
# faster than 36.69% of Python3
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:                       
        return 0  
    
    i = j = 0
    word = set()
    maxlen = 0
    while i < len(s) and j < len(s):
        # print(s[i], s[j], word)
        if s[j] in word:
            word.remove(s[i])
            i = i + 1
        else:
            maxlen = max(maxlen, j - i + 1)
            word.add(s[j])
            j = j + 1
    return maxlen


'''
# 动态规划 当要记录一段长度的技巧：
# dp[j] = i 表示子串s[i…j]是以s[j]字符为结尾
'''

'''
代替remove和add的方式就是用map记录位置，用位置卡remove掉的
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength