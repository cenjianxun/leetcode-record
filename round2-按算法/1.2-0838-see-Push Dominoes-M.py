'''
838. Push Dominoes
Medium

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
'''

'''
好笨的的方法
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # L = -1, R = 1, . = 0
        mapping = {'L': -1, 'R': 1, '.': 0}
        pushLtoR, pushRtoL = [0] * len(dominoes), [0] * len(dominoes)
        push = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                push = mapping[dominoes[i]]
            if dominoes[i] == 'L':
                push = 0
            if push == 0:
                pushLtoR[i] = mapping[dominoes[i]]
            else:
                if dominoes[i] == 'R':
                    pushLtoR[i] = mapping[dominoes[i]]
                else:
                    push = push + 1
                    pushLtoR[i] = push
                    
        push = 0
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == 'L':
                push = mapping[dominoes[i]]
            if dominoes[i] == 'R':
                push = 0
            if push == 0:
                pushRtoL[i] = mapping[dominoes[i]]
            else:
                if dominoes[i] == 'L':
                    pushRtoL[i] = mapping[dominoes[i]]
                else:
                    push = push - 1
                    pushRtoL[i] = push  
                    
        # print(pushLtoR)
        # print(pushRtoL)
        res = []
        for i in range(len(dominoes)):
            F = pushLtoR[i] + pushRtoL[i]
            if pushLtoR[i] * pushRtoL[i] >= 0 or F == 0:
                if F < 0:
                    res.append('L')
                if F > 0:
                    res.append('R')
                if F == 0:
                    res.append('.')
            else:
                if F > 0:
                    res.append('L')
                if F < 0:
                    res.append('R')
        return ''.join(res)

'''
good 官方
'''
class Solution:
    def pushDominoes(self, d: str) -> str:
        res = list(d)
        symbols = [(-1,'L')] + [(i, x) for i, x in enumerate(d) if x != '.'] + [(len(d), 'R')]
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    res[k] = x
            elif x > y:
                for k in range(i+1, j):
                    if k - i > j - k:
                        res[k] = 'L'
                    if k - i < j - k:
                        res[k] = 'R'
                    if k - i == j - k:
                        res[k] = '.'
        return ''.join(res)