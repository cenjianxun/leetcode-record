'''
828. Count Unique Characters of All Substrings of a Given String
Hard

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

    Input: s = "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    Every substring is composed with only unique letters.
    Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

    Input: s = "ABA"
    Output: 8
    Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Example 3:

    Input: s = "LEETCODE"
    Output: 92
 
Constraints:

    1 <= s.length <= 105
    s consists of uppercase English letters only.
'''

'''
超时

动归没搞懂
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        subCount = {}
        res = 0
        for i in range(len(s)):
            visited = {}
            unique = 0
            for j in range(i, len(s)):
                if s[j] not in visited:
                    unique += 1 
                elif visited[s[j]] == 1:
                    unique -= 1
                visited[s[j]] = visited.get(s[j], 0) + 1        
                #print(s[i:j+1], unique)
                res += unique

        return res

'''
以每个字符为中心，向两边扩展到不重复为止，左右长度乘积即为该字符出现的次数。
例如:
ABCDE 位于A时，左边为A，右边有A,AB,ABC,ABCD,ABCDE五种情况，15，说明有五个A。
位于C时，左边有C,BC,ABC三种情况，右边有C,CD,CDE三种情况，33=9。如下图
C CD CDE
C C CD CDE
BC BC BCD BCDE
ABC ABC ABCD ABCDE
以此类推，计算出总数。

作者：spacex
链接：https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/solution/zhao-gui-lu-by-spacex/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left , right = i - 1, i + 1
            while left > - 1 and s[i] != s[left]:
                left -= 1
            while right < len(s) and s[i] != s[right]:
                right += 1
            res += (i - left) * (right - i)
        return res        