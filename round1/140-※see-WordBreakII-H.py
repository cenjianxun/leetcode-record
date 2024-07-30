'''
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
其实有点像 用key标记用过的，用value记录值
'''

'''
嘿嘿竟然用上一个超时的dps可以
'''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordmap = defaultdict(set)
        for word in wordDict:
            wordmap[word[0]].add(word)

        def helper(s, onebreak):
            if not s:
                res.append(' '.join(onebreak))
                return 
            for word in wordmap[s[0]]:
                if word == s[:len(word)]:
                    helper(s[len(word):], onebreak + [word])
        helper(s, [])
        return res

'''
139和140的区别，139求是否可用被拆分，140求所有拆分结果

如果用例
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

第一轮循环里，i = 0，因为s[0]在wordDict中，所以会递归分析s[1:]的内容，又因为s[1]也在wordDict中，所以会继续递归s[2:]的内容……以及后续的递归
在下一轮循环里，此时i = 1，因为s[1]在wordDict中，所以会递归s[2:]的内容……
于是问题就出现了，明明在第一轮循环里已经发现s[2:]是无法按照字典里的单词分割的，在第二轮循环里又要对s[2:]重新查找。当然还有后续的s[3:],s[4:]等等。整个计算的复杂度是指数级别的，这显然是无法接受的。

那么应该怎么进行优化呢？假如说我在第一轮循环里计算完s[2:]的内容无法分割，然后我在小本本上记下s[2:]是无法分割的，那么后续再遇到这个问题的时候，计算机就不会再去查找了。
具体方法是申请一个备忘录数组，就是我们的小本本。memo[i:]代表了s[i:]这个字符串能否被分割，如果不能，那就停止后续的所有遍历
 
第二种：
仍然使用dp，但dp里不是存放bool，而是集合，存放当前可拆放的单词们
'''