'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''



'''
做两次判断，一次是mid和start、end的判断，一次是target和target边界的判断

要找到target的边界，就是说从mid、start、end里取它的边界。
可以先判断start mid， mid end哪个是单调的
这里要注意 必须是start<=mid 和 mid < end, 因为mid可以取到left值，不能取到right值

如果这个区间的left值 < right值，说明它单调；在它单调的基础上，如果target在这个单调区间里，就可以把start、end两个边界缩小到这个区间里，否则就把目标锁赶离这个区间。

bug: while时要加=
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            print(start, end, mid)
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1