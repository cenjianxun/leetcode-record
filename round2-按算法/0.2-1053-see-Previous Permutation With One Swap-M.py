'''
1053. Previous Permutation With One Swap
Medium

Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.

Example 1:

	Input: arr = [3,2,1]
	Output: [3,1,2]
	Explanation: Swapping 2 and 1.

Example 2:

	Input: arr = [1,1,5]
	Output: [1,1,5]
	Explanation: This is already the smallest permutation.

Example 3:

	Input: arr = [1,9,4,6,7]
	Output: [1,7,4,6,9]
	Explanation: Swapping 9 and 7.
 
Constraints:

	1 <= arr.length <= 104
	1 <= arr[i] <= 104
'''

'''
倒着找第一组（顺着看）降序的两个值
高峰就是start被替换的那个，然后依着这个高峰值，找后面比它小的最大值，如果有好几个，优先找index小的
'''
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)-1, -1, -1):
            if stack:
                if arr[i] <= arr[stack[-1]]:
                    stack.append(i)
                else:
                    break
            else:
                stack.append(i)
        print(stack)
        if stack[-1] == 0:
            return arr
        start = stack[-1] - 1
        end = len(arr)
        for i in stack:
            if arr[i] < arr[start]:
                if end == len(arr) or arr[i] >= arr[end]:
                    end = i
        arr[start], arr[end] = arr[end], arr[start]
        return arr