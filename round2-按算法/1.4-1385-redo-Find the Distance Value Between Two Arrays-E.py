'''
1385. Find the Distance Value Between Two Arrays
Easy

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

	Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
	Output: 2
	Explanation: 

Example 2:

	Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
	Output: 2

Example 3:

	Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
	Output: 1
 
Constraints:

	1 <= arr1.length, arr2.length <= 500
	-1000 <= arr1[i], arr2[j] <= 1000
	0 <= d <= 100
'''

'''
arr1的值：最长的竖条
arr2：▪
范围 ┣━━┫ 是-d 到 +d
▪ 不能落入┣━━┫
┃的位置不变，如果点在┃━┫的右边，说明点找大了，反之找小了。
        ┃
▪     ┣━╋━┫ ▪      ▪
        ┃

'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        #print(arr2)
        def validDis(num, arr, d):
            lo, hi = 0, len(arr) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if abs(arr[mid] - num) <= d:
                    return False
                if arr[mid] > d + num:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if lo > hi:
                return True
        
        for num in arr1:
            if validDis(num, arr2, d):
                res += 1
            #print(num, res)
        return res