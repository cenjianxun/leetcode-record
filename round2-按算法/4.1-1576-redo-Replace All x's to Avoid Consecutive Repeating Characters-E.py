'''
1576. Replace All ?'s to Avoid Consecutive Repeating Characters
Easy

Share
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Constraints:

1 <= s.length <= 100
s consist of lowercase English letters and '?'.
'''

'''
只需要3种字符abc就可以完成整个的替换。总是替换成前一个字符的下一个字符，如果该字符等于后一个字符，那么替换为后一个 字符的下一个字符。这样的替换不会出现矛盾，因为？总是可以选择一种字符来替换，且不会产生冲突
'''
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for c in 'abc':
				    if (i == 0 or s[i - 1] != c) and (i + 1 == len(s) or s[i + 1] != c):
					    s[i] = c
					    break
        return ''.join(s)