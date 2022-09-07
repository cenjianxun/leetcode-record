'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

'''
不知道有什么其他的解法
'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word = set()
        self.prefix_word = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.word.add(word)
        prefix = ''
        for w in word:
            prefix = prefix + w

            self.prefix_word.add(prefix)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # print(prefix, self.prefix_word)
        if prefix in self.prefix_word:
            return True
        else:
            return False

'''
字典树，需要一个node，node的child是字典，值是node
然后字典套字典。
另外字典还需要一个字符串，标记是在半路还是一个完整的word
'''
class Node(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            if not w in current.children:
                current.children[w] = Node()
            current = current.children[w]
        current.isEnd = True
        print('insert', current.children)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            if not w in current.children:
                return False
            current = current.children[w]
        return current.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            if not w in current.children:
                return False
            current = current.children[w]
        return True