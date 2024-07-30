'''
154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:

    Input: nums = [1,3,5]
    Output: 1

Example 2:

    Input: nums = [2,2,2,0,1]
    Output: 0

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
'''

'''
和153的区别是有重复。
有重复产生的区别是：中值可能与边值相等
当相等的时候，只能-1

此外，因为可能相等，所以只能和nums[end]比较，而不能只和定值nums[-1]比较
153比两个都可以。

为什么比较mid与right而不比较mid与left？
具体原因前面已经分析过了，简单讲就是因为我们找最小值，要偏向左找，目标值右边的情况会比较简单，容易区分，所以比较mid与right而不比较mid与left
[456123]因为往右比，是单调的所以简单

如果是选最大值，就往左边比

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end = end - 1
        return nums[start]

'''
# 153:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid - 1 >= 0 and nums[mid] < nums[mid -1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
'''

