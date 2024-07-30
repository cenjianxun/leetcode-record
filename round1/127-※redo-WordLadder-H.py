'''
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''

'''
使用bfs解题
'''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # 不重复的元素串合集
        alphas = ''.join(set(list(reduce(lambda x, y: x+y, wordList))))
        # print(alphas)
        wordset = set(wordList) #- {beginWord}
        queue = deque([(beginWord, 1)])
        while queue:
            # print(queue)
            word, lens = queue.popleft()
            if word == endWord:
                return lens
            # print(word, queue, wordset)
            for i in range(len(word)):
                for c in alphas:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordset:
                        wordset.remove(new_word)
                        queue.append((new_word, lens + 1))
        return 0




'''
超时
'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        L = len(wordList)
        dp = [[0] * L for _ in range(L)]
        for i in range(L):
            for j in range(L):
                dp[i][j] = self.diffnum(wordList[i], wordList[j])

        path = float('inf')
        def helper(word, pathset, path):
            
            if endWord in pathset:
                print(endWord, pathset)
                return min(path, len(pathset))
            index = wordList.index(word)
            for i in range(L):
                if dp[index][i] == 1 and wordList[i] not in pathset:
                    path = min(path,helper(wordList[i], pathset | {wordList[i]}, path))
            return path
            
        #print(dp)
        for i in range(L):
            if self.diffnum(beginWord, wordList[i]) == 1:
                p = helper(wordList[i], {wordList[i]}, path)
                if p:
                    path = min(path, p)
        return  path + 1 if path < L else 0
        
    def diffnum(self, word1, word2):
        i = 0
        num = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                num += 1
            i += 1
        return num + abs(len(word1) - len(word2))