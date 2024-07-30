'''
658. Find K Closest Elements
Medium

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:

	Input: arr = [1,2,3,4,5], k = 4, x = 3
	Output: [1,2,3,4]
Example 2:

	Input: arr = [1,2,3,4,5], k = 4, x = -1
	Output: [1,2,3,4]
 
Constraints:

	1 <= k <= arr.length
	1 <= arr.length <= 104
	arr is sorted in ascending order.
	-104 <= arr[i], x <= 104
'''

'''
考虑成（减去k后的绝对值）区间左右两侧端点哪个离0更近

注意hi的值是 len-k 而不是len-k-1，因为hi值是左边界的右边界，即，左边界可取值从[lo, hi]
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (x - arr[mid]) > (arr[mid + k] - x):
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]