'''
85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
'''

'''
每一行分别leetcode 84

在进栈出栈的时候
1.宽，即左侧不是按当前出栈的i定的，（高倒是按出栈的i的值定得）而是按出栈后，stack里最后一个值的i定的，是它的右侧
2. 所以要分情况，栈为空以及不为空，为空时是i-0，即直接是i本身，
'''
# faster than 99.47% of Python3
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        heights = [0] * (len(matrix[0]) + 1)
        for i in range(len(matrix)):  
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] = heights[j] + 1
            # print(i, heights)
            res = max(res, self.getArea(heights))
        return res
    
    def getArea(self, heights):
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                w = i if not stack else i - stack[-1] - 1
                res = max(res, heights[j] * w)

            stack.append(i)
            # print(i, res, stack)
        return res   