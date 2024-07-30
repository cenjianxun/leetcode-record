'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''


# def maxArea(height: List[int]) -> int:
#     if len(height) < 2:
#         return 0
#     hlist = []
#     for i in range(0, len(height)):
#         hlist.append(0)
#         for j in range(0, len(height)):
#             if height[j] >= height[i]:
#                 hlist[i] = hlist[i] if hlist[i] > abs(j-i) * height[i] else abs(j-i) * height[i]
#     return max(hlist)

'''
暴力法会超时 ↑

思路：
因为：需要长度尽量长 + 高度尽量高 h * (j - i)
两个因子，so 两种
1. 先选高度最高的，再慢慢抻长长度缩短高度，在活动过程中h都是当前最大
2. 先选长度最长的，再慢慢缩短长度提高高度, 在活动过程中j-i都是当前最大

选2：
在从两端缩短长度的时候，选较短的那个缩，因为h按短的定的，如果一直换长的，area只会越来越小。

'''

def maxArea(height):
    if len(height) < 2:
        return 0
    area = 0
    head = 0
    tail = len(height) - 1
    while head < tail:
        if height[head] >= height[tail]:
            h = height[tail]
            w = tail - head
            tail = tail - 1
        else:
            h = height[head]
            w = tail - head
            head = head + 1
        area = max(area, w * h)
        print(area)
    return area

maxArea([1,8,6,2,5,4,8,3,7])

'''
想起了 这个方法
根髓是和3sum一样的。同时挪两边
'''
def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    while i < j:
        w = j - i
        if height[i] > height[j]:
            h = height[j]
            j = j - 1
        else:
            h = height[i]
            i = i + 1
        area = max(area, w * h)
    return area