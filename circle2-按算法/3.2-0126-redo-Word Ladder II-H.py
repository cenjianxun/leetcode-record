'''
126. Word Ladder II

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

	Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
	Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
	Explanation: There are 2 shortest transformation sequences:
	"hit" -> "hot" -> "dot" -> "dog" -> "cog"
	"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

	Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
	Output: []
	Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
Constraints:

	1 <= beginWord.length <= 5
	endWord.length == beginWord.length
	1 <= wordList.length <= 500
	wordList[i].length == beginWord.length
	beginWord, endWord, and wordList[i] consist of lowercase English letters.
	beginWord != endWord
	All the words in wordList are unique.
'''

'''
超时
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        res = []
        queue = deque([([beginWord], 1)])
        shortest = float('inf')
        while queue:
            
            path, step = queue.popleft()
            if path[-1]==endWord:
                shortest = min(shortest, step)
                res.append((path, step))
                continue
            for word in wordList:
                if word not in path:
                    dif = self.countdif(path[-1], word)
                    if dif == 1 and len(path)+1 <=shortest:
                        queue.append((path + [word], step+1))
    
        return [path for path, step in res if step == shortest]
        
        
    def countdif(self, a, b):
 
        if a == b:
            return 0
        if len(a) > len(b):
            a, b = b, a
        i = 0
        count = 0
        while i < len(a):
            if a[i] != b[i]:
                count += 1
            i += 1
        return count + len(b) - i

'''
还是超时

比较相同的时候，可以拼凑它再看它是否在原set里
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        res = []
        alphas = ''.join(set(list(reduce(lambda x, y: x+y, wordList))))
        queue = deque([([beginWord], 1)])
        shortest = float('inf')
        while queue:          
            path, step = queue.popleft()
            word = path[-1]
            if word == endWord:
                shortest = min(shortest, step)
                res.append((path, step))
                continue
            for i in range(len(word)):
                for w in alphas:
                    new_word = word[:i] + w + word[i+1:]
                    if new_word in wordset and len(path) + 1 <= shortest:
                        #print(word, new_word)
                        queue.append((path + [new_word], step+1))
    
        return [path for path, step in res if step == shortest]

'''
超时
idea：
每一轮把同样的step都弄完，因为同一step的word只不能出现在之前的visited里，所以同一轮要单设一个visited
while的时候跳出循环要多设一个，如果有res就 跳出。    
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        letters = ''.join(set(list(''.join(wordList))))
        queue = deque([[beginWord]])
        visited = set([beginWord])
        res = []
        while queue and not res:
            lens = len(queue)
            localVisited = set()
            for _ in range(lens):
                path = queue.popleft()
                word = path[-1]
                for i in range(len(word)):
                    for w in letters:
                        newWord = word[:i] + w + word[i+1:]
                        if newWord == endWord:
                            res.append(path+[newWord])
                        if newWord in wordSet and newWord not in visited:
                            queue.append(path+[newWord])
                            localVisited.add(newWord)
            visited = visited.union(localVisited)
        return res
