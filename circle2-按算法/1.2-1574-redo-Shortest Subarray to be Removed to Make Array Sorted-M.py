'''
1574. Shortest Subarray to be Removed to Make Array Sorted
Medium

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example 1:

	Input: arr = [1,2,3,10,4,2,3,5]
	Output: 3
	Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
	Another correct solution is to remove the subarray [3,10,4].

Example 2:

	Input: arr = [5,4,3,2,1]
	Output: 4
	Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

	Input: arr = [1,2,3]
	Output: 0
	Explanation: The array is already non-decreasing. We do not need to remove any elements.
 
Constraints:

	1 <= arr.length <= 105
	0 <= arr[i] <= 109
'''

'''
切分三段，左边递增 + 中间 + 右边递增
* 1. 最后要比较（-中间-右边）、（-左边-中间）、（-中间-两边非递增的）中间的最小值
* 2. 整列递增要单独考虑
* 3. 因为要求最小值，所以左++优先
* 4. 注意取值，尤其是left，是选最大的还是选下一个最小的([1,3,5,2]，left = 5还是2)要拿定主意
    这里选的是2，所以后面i是<l 而不是<=2。
* 5. j-i还要-1
'''
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 1
        while l < len(arr) and arr[l - 1] <= arr[l]:
            l += 1
        if l == len(arr):
            return 0
        r = len(arr) - 1
        while r - 1 >= 0 and arr[r] >= arr[r - 1]:
            r -= 1
 
        res = len(arr)
        i, j = 0, r
        while i < l and j < len(arr):
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1             
            else:
                j += 1
                
        return min(res, r, len(arr) - l)
