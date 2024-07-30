'''
https://www.geeksforgeeks.org/count-subarrays-with-consecutive-elements-differing-by-1/

Given an array arr[] of N integers. The task is to count the total number of subarrays of the given array such that the difference between the consecutive elements in the subarrays is one. That is, for any index i in the subarrays, arr[i+1] – arr[i] = 1.
Note: Do not consider subarrays with a single element.

Examples:

Input : arr = [1, 2, 3]
Output : 3
The subarrays are {1, 2}. {2, 3} and {1, 2, 3}

Input : arr = [1, 2, 3, 5, 6, 7]
Output : 6
'''

def CountSubArr(arr):
	res = 0
	i = 0
	count = 1
	arr.sort()
	arr.append(float('inf'))
	while i < len(arr) - 1:
		print(i, count)
		if arr[i+1] - arr[i] == 1:
			count += 1
		elif count > 1:
			res += countASub(count)
			count = 1
		i += 1
	print(res)
	return res

def countASub(n):
	if n == 2:
		return 1
	return countASub(n-1) + n - 1

arr = [1, 2, 3, 5, 6, 7]
CountSubArr(arr)