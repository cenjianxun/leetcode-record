'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''

'''
注意边界条件
'''

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(0, n):
        nums1[m+i] = nums2[i]
    # nums1.sort()
    i = 0
    j = m
    
    while i< j and j < m + n:
        print('nums1',nums1)
        if nums1[i] <= nums1[j]:
            i = i + 1
        else:
            temp = nums1[j]
            nums1[i+1:j+1] = nums1[i:j]
            nums1[i] = temp
            i = i + 1
            j = j + 1

'''
可以倒着
'''