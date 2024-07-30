'''
https://leetcode.com/problems/reorder-data-in-log-files/

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:
1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.
'''

'''
key=cmp_to_key(f)
f:升序<0
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, letter = [], []
        for i, log in enumerate(logs):
            if log.split(' ')[-1].isdigit():
                digit.append(i)
            else:
                letter.append(log)
    
        def compare(a, b):
            a0, a1 = a.split(' ', 1)
            b0, b1 = b.split(' ', 1)
            if a1 < b1:
                return -1
            elif a1 > b1:
                return 1
            else:
                if a0 < b0:
                    return -1
                else:
                    return 1
        print(letter)
        res = sorted(letter, key=cmp_to_key(compare))
        for i in digit:
            res.append(logs[i])
        return res