'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''


'''
用trie
'''
class Node:
    def __init__(self):
        self.child = {}
        self.isEnd = ''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not len(board):
            return []
        trie = self.Trie(words)
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.DFS(board, i, j, trie)
        return self.res
        
    def DFS(self, board, i, j, trie):
        if trie.isEnd:
            self.res.append(trie.isEnd)
            trie.isEnd = ''

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or not board[i][j] in trie.child:
            return 

        tmp, board[i][j] = board[i][j], 'X'
        for dx, dy in zip((1, -1, 0, 0), (0, 0, 1, -1)):
            self.DFS(board, dx + i, dy + j, trie.child[tmp])
        board[i][j] = tmp
    
    def Trie(self, words):
        root = Node()
        for word in words:
            cur = root
            for w in word:
                if not w in cur.child:
                    cur.child[w] = Node()
                cur = cur.child[w]
 
            cur.isEnd = word
 
        return root


'''
220617

坑多。
1. 如果board少，word多，表示不能用重复的格子 [['a']] 'aaa'
2. 如果words里面有重复的字母，也得留着。所以不能在原board中标记改动
3. 如果board里面有不同的地方都能满足word，答案里面也不能出现重复的word

dfs超时
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                for word in words:
                    if board[i][j] == word[0] and self.isExist(i, j, board, word[1:], {(i, j)}):
                        res.add(word)
        return res
    
    def isExist(self, i, j, board, word, visited):
        #print(i,j,word,visited)
        if not word:
            return True
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <=x < len(board) and 0 <= y < len(board[0]) and (x,y) not in visited:
                if board[x][y] == word[0] and self.isExist(x, y, board, word[1:], visited | {(x,y)}):
                    return True
        return False

'''
用trie，仍然要注意 dfs里， i,j 判定边界是在循环里还是在循环外 [['a']] 'a'
找到之后要把isword标'', 否则会找到许多重复的
board[i][j] 还是要替换，否则会报错
'''
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isWord = ''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = self.getTrie(words)
        
        def dfs(i, j, trie):
            if trie.isWord:
                res.append(trie.isWord)
                trie.isWord = ''
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie.child:
                return
            w, board[i][j] = board[i][j], 0
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:     
                dfs(x, y, trie.child[w])
            board[i][j] = w
                  
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie)
        return res
        
    def getTrie(self, words):
        root = TrieNode()      
        for word in words:
            cur = root
            for w in word:
                cur = cur.child[w]
            cur.isWord = word
        return root