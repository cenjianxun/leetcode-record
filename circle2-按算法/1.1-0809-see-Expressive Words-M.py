'''
809. Expressive Words

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.


Example 1:

	Input: s = "heeellooo", words = ["hello", "hi", "helo"]
	Output: 1
	Explanation: 
	We can extend "e" and "o" in the word "hello" to get "heeellooo".
	We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
	Example 2:

	Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
	Output: 3

Constraints:

	1 <= s.length, words.length <= 100
	1 <= words[i].length <= 100
	s and words[i] consist of lowercase letters.
'''
 
'''
很多小点：
1. 相同的词必须连着
2. 不能有对方没出现过的词
3. 两个里面的词要么一样长，要么，s该词的个数不能小于word里的，要么必须大于2个
4. 不能一个数完了另一个没数完

'''
# faster than 5.07% of Python3
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        
        def isvalid(word):
            i = j = 0
            while i < len(s) or j < len(word):
                
                if i == len(s) or j == len(word) or s[i] != word[j]:
                    return False
                print(s[i], word[j])
                counti = countj = 0
                while i + counti < len(s) and s[i] == s[i + counti]:
                    counti += 1
                while j + countj < len(word) and word[j] == word[j + countj]:
                    countj += 1 
                if counti < countj or counti > countj and counti < 3:
                    return False
                
                i, j = i + counti, j + countj
    
            return True
            
        for word in words:
            if set(word) - set(s) or set(s) - set(word):
                break
            
            if isvalid(word):
                res += 1
                
        return res

'''
sample:
用一些函数和数据结构表现和存储压缩过的词
'''
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def process(st):
            if not st:
                return [], []
            chars, counts = [st[0]], [1]
            
            for i in range(1, len(st)):
                if st[i] == chars[-1]:
                    counts[-1] += 1
                else:
                    chars.append(st[i])
                    counts.append(1)
            return chars, counts
                

        ans = 0
        s_chars, s_counts = process(S)
        for word in words:
            w_chars, w_counts = process(word)
            
            if s_chars == w_chars:
                counter = 0
                for k in range(len(w_chars)):
                    if w_counts[k]==s_counts[k] or (w_counts[k]<s_counts[k] and s_counts[k]>=3):
                        counter += 1
                
                if counter ==len(w_chars):
                    ans += 1

        return ans