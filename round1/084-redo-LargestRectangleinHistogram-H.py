'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

'''
它的精髓是：
如果是升，就一直进栈，因为面积仍有可能增加
如果是降（比当前的i高），就逐一弹出比当前i高的，然后倒着计算、比较面积，
面积就是，高为当前pop出的值，宽为:以i左边为右边界(意思是不带i)，以pop完之后的栈里的最后一个index的右边为左边界(意思是也不带那个最后一个index)
因为倒着来，因为栈里是非降的，遍历至当前的面积的高就是pop出的那个，宽就是pop出的左边至i之前。
* 然后 i else i - stack[-1] - 1
就是说，如果当前stack里没有比当前的i低的了，就一直通到底，因为如果有比它低的，就会挡在第一个，作为左边界。
那些更高的，就已经拔掉了，因为就算拔掉了，高的的下半身仍然可以持续存在组成area。

另外一个点是需要给heights原数组里添加一个高为0的在最后，方便算本来的最后一个值。因为是算当前i以前的，所以如果要算最后一个值，要站在比最后一个值更右的一个地方。
'''
def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    res = 0
    heights.append(0)
    N = len(heights)
    for i in range(N):
        # print(i, heights[i], stack, res)
        while stack and heights[i] <= heights[stack[-1]]:
            h = heights[stack.pop()]
            
            w = i if not stack else i - stack[-1] - 1
            res = max(res, h * w)
        stack.append(i)
    return res


# ----------
'''
↑↑↑ while里计算的是被pop出的内容的面积
❗❗❗ 为什么在while循环里，的左边界是pop完之后，stack的最后一个，而不是被pop的那个本身，
是因为，单调（升）栈，i的左边两种情况：无了，或是比i还大的值，那么要往左边延申的话，不在栈里的那些是应该要被算进去的（因为比i大），所以左边界不是i本身，而是i之前的一个值k（<— k是第一个不满足、不能算的值）的后一位

暴力解法：本质是，对每一个元素，左右延展比它高的，为宽，它自己为高。
要注意的点是：
while里面左右边界判断退出是，是不满足👆条件，不被包含在w里的那边边界，所以在算宽的时候不能把它俩算进去
'''
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    res = 0
    for i in range(len(heights)):
        left = right = i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1
        while right < len(heights) and heights[right] >= heights[i]:
            right += 1
        res = max(res, heights[i] * (right - left - 1))
        # print(left, i, left, res)
    return res