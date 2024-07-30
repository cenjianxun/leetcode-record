'''
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
'''

'''
???
'''
def findPeakElement(nums: List[int]) -> int:
    n = max(nums)
    return nums.index(n)


'''
1. 顺序查找，从1到 len - 2里顺序比较nums[i] >= nums[i - 1] && nums[i] >= nums[i + 1]
2. 找全局最大值
3. 二分法：left, right, mid1, mid2。 比较mid1和mid2, 然后缩小左右，最终只有左右。

看清比较是比较mid和mid+1还是mid和start/end

follow up:
在二位数组里找峰值
1. 全局遍历最大值
2. 二分法：找每行最大值，再用每行最大找该列最大
3. 找田字：https://www.jb51.net/article/137688.htm
'''

def findPeakElement(nums: List[int]) -> int:

    left, right = 0, len(nums) - 1
    while left < right:
        mid = int((left+right)//2)
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid 
    return left


'''
递归不行的原因是 递归后的新nums边界自动为-无穷，且新index不一定=原index
👆 left 如果是 =mid的话，递归就永远出不去
'''