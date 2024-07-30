'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''


def isMatch(s: str, p: str) -> bool:
    ls = len(s) + 1
    lp = len(p) + 1
    dp = [lp * [False] for _ in range(ls)]
    
    dp[0][0] = True
    
    for n in range(1, lp):
        if p[n-1] == '*':
            dp[0][n] = dp[0][n-2]
            
    for i in range(1, ls):
        for j in range(1, lp):
            # print(i,s[i-1],j, p[j-1])
            if p[j-1] in (s[i-1], '.'):
                dp[i][j] = dp[i-1][j-1]
                print('==   ',i-1,s[i-1],j-1, p[j-1], dp[i][j])
            else:
                if p[j-1] == '*':
                    if p[j-2] in (s[i-1], '.') or dp[i][j-2]:
                        dp[i][j] = dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
                        print('not *',i-1,s[i-1],j-1, p[j-1], dp[i][j])
                print('not  ',i-1,s[i-1],j-1, p[j-1], dp[i][j])

    # print(dp)      
    return dp[ls-1][lp-1]
                
s = "mississippi"#'aaa'#"mississippi"
p = "mis*is*p*."#'ab*ac*a'#"mis*is*p*."
result = isMatch(s, p)
print(result)

'''
从前往后
两种情况： 1. 相等或等于'.' 2. == '*'
2有三种情况：① 不匹配 ②匹配一个 ③匹配多个
因为是从前往后，所以匹配一个和匹配多个可以合并
'''
def isMatch(self, s: str, p: str) -> bool:
    if not p:
        return not s
    ifmatch = s and p[0] in (s[0], '.')
    if len(p) > 1 and p[1] == '*':
        return self.isMatch(s, p[2:]) or ifmatch and self.isMatch(s[1:], p)
    else:
        return ifmatch and self.isMatch(s[1:], p[1:])


'''
注意的点：
1. 横纵都多一
2. 点00为1
3. 第一行要单独处理，即s为空，匹配不同的patten
4. p和s的index 和dp的index不同！dp的往后+1位，因为最开始在开头加了一行
5. 也是分情况 == '*'的里面，再分两种，
i-1匹配：in (s[i], '.') 
和 i-1不相等：p[j-1] != s[i]
在匹配的分支里，当前dp又由两个决定，
s的上一个dp[i][j+1]，
和p的前两个dp[i+1][j-1],即x*匹配空
'''
def isMatch(self, s: str, p: str) -> bool:
    dp = [[0 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(p)):
        if p[i] == '*':
            dp[0][i+1] = dp[0][i-1]
    # print(dp)
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] in (s[i], '.'):
                dp[i+1][j+1] = dp[i][j]
            elif p[j] == '*':
                if p[j-1] in (s[i], '.'):
                    # print(i,j,dp[i][j+1])
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j-1] #or dp[i][j-1]
                elif p[j-1] != s[i]:
                    dp[i+1][j+1] = dp[i+1][j-1]
    # print(dp)
    return dp[-1][-1]