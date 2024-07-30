'''
68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 
Example 1:

	Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
	Output:
	[
	   "This    is    an",
	   "example  of text",
	   "justification.  "
	]

Example 2:

	Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
	Output:
	[
	  "What   must   be",
	  "acknowledgment  ",
	  "shall be        "
	]
	Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
	Note that the second line is also left-justified because it contains only one word.
	Example 3:

	Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
	Output:
	[
	  "Science  is  what we",
	  "understand      well",
	  "enough to explain to",
	  "a  computer.  Art is",
	  "everything  else  we",
	  "do                  "
	]
 
Constraints:

	1 <= words.length <= 300
	1 <= words[i].length <= 20
	words[i] consists of only English letters and symbols.
	1 <= maxWidth <= 100
	words[i].length <= maxWidth
'''

'''
要注意不是最后一行但是只有一个单词的：除数space_num变成了0
'''
# faster than 17.30% of Python3
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        while words:
            aline = []
            while words and len(' '.join(aline)) < maxWidth:
                aline.append(words.pop(0))
            if len(' '.join(aline)) > maxWidth:
                words.insert(0, aline.pop())
            if words:
                aline = self.justified(aline, maxWidth)
            else:
                aline = ' '.join(aline)
                aline = aline + ' ' * (maxWidth - len(aline))
            res.append(aline)
        return res
    
    def justified(self, aline, maxWidth):
        space_num = len(aline) - 1
        space_sum = maxWidth - len(''.join(aline))
        if space_num:
            div, rest = space_sum//space_num, space_sum%space_num
            space = [' ' * div] * space_num
            i = 0
            while i < rest:
                space[i] += ' '
                i += 1
            res = [''] * (len(aline) + space_num)
            res[::2], res[1::2] = aline, space
            return ''.join(res)
        else:
            return aline[0] + ' ' * space_sum