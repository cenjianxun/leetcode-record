'''
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:

	Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
	Output: true
	Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

	Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
	Output: false
	Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

	Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
	Output: false
	Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
Constraints:

	1 <= words.length <= 100
	1 <= words[i].length <= 20
	order.length == 26
	All characters in words[i] and order are English lowercase letters.
'''

'''
值得看一眼，分支众多
1. 只要第一个字母小，就成立
2. 如果相等才继续
3. 如果循环完了还要比较尾巴，前一个数有尾巴就是错的。或者可以把两数用' '对齐，且把' '加到order最前
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pre = words.pop(0)
        for word in words:
            for i in range(min(len(pre), len(word))):
                #print(word, i, order.index(pre[i]) , order.index(word[i]))
                if order.index(pre[i]) < order.index(word[i]):
                    pre = word
                    break
                if order.index(pre[i]) == order.index(word[i]):
                    continue
                if order.index(pre[i]) > order.index(word[i]):
                    return False
            if len(pre) > len(word):
                return False
            pre = word
        return True