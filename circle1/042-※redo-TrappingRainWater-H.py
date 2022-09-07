'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''



def calArea(L):
    area = 0
    h = min(L[0],L[-1])
    for l in L:
        if l < h:
            area = h - l + area
    return area

def trap(height) -> int:
    area = 0
    if len(height) < 2:
        return area
    left, mid, right = 0, 1, 2
    while right < len(height):
        while left < len(height) - 2 and height[left] <= height[left+1]:
            left = left + 1
        mid = left + 1
        while mid < len(height) -1 and height[mid] >= height[mid+1]:
            mid = mid + 1
        right = mid + 1
        for r in range(right, len(height)):
            if height[r] > height[left]:
                right = r
                break
            if height[r] > height[right]:
                right = r
        if left < mid < right < len(height) and height[mid] < height[left] and height[mid] < height[right]:
            area = calArea(height[left:right+1]) + area
            left = right
            mid = right + 1
            right = right + 2
    return area

h = [0,1,0,2,1,0,1,3,2,1,2,1]
r = trap(h)
print(r)


'''
好想法：是往右边投射的面积和往左边投射的面积的交集
'''

def trap(self, height: List[int]) -> int:
    leftmax = [0] * len(height)
    high = 0
    for i in range(len(height)):
        if height[i] > high:
            high = height[i]
        leftmax[i] = high
    area = 0
    high = height[-1]
    for i in range(len(height) - 1, -1, -1):
        if height[i] > high:
            high = height[i]
        if min(high, leftmax[i]) > height[i]:
            area = area + min(high, leftmax[i]) - height[i]
            
    return area

'''
递归：要两边夹逼[2,1,0,4], 找中值的时候也要找到里面最大的。
要注意的点是：
r-l 在过滤之后距离要超过2否则返回
index如果是slice要指定起始位置！
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        def findTrap(l, r):
            area = 0

            while l < r and height[l] <= height[l+1]:
                l += 1
            while l < r and height[r] <= height[r-1]:
                r -= 1
            if r - l < 2:
                return area
            mid = height.index(max(height[l+1:r]), l+1)
            h = min(height[l], height[r])
            #print(l, r, mid)
            if height[mid] < h:
                for i in range(l+1, r):
                    area += h - height[i]
            else:
                area += findTrap(l, mid) + findTrap(mid, r)
            return area      
        return findTrap(0, len(height)-1)