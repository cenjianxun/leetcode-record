'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

class Solution:
    def addGen(self, gen):
        l = set()
        l.add('()' + gen)
        l.add(gen + '()')
        # l.add('(' + gen + ')')
        i = 0
        while gen and i < len(gen) - 1:
            if gen[i] == '(':# and gen[i+1] == ')':
                l.add(gen[0:i+1] + '()' + gen[i+1:])
            i = i + 1
        return l
        
    def subGen(self, preL):
        l = []
        for g in preL:
            l.extend(list(self.addGen(g)))
        return set(l)
    
    def generateParenthesis(self, n):
        result = []

        if not n:
            return result
        if n == 1:
            result.extend(list(self.addGen('')))
        if n > 1:
            result.extend(list(self.subGen(self.generateParenthesis(n-1))))
        return list(set(result))

s = Solution()
result = s.generateParenthesis(7)
print(result)

'''
可以用递归，dfs，bfs
'''