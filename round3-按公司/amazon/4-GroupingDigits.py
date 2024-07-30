'''
Given an array of binary digits, 0 and 1, sort the array so that all zeros are at one end and all ones are at the other. Which end does not matter. To sort the array, swap any two adjacent elements. Determine the minimum number of swaps to sort the array.

Example
arr = [0, 1, 0, 1]
With 1 move, switching elements 1 and 2 yields [0, 0, 1, 1], a sorted array

Function Description
Complete the function minMoves

minMoves has the following parameter(s):
int arr[n]: an array of binary digits

Returns
int: the minimum number of moves necessarry

Constraints

1 <= n <= 10^5
arr[i] is in the set {0, 1}
Another Example
arr = [1, 1, 1, 1, 0, 0, 0 0]
We return 0 because we do not need to swap any elements
'''

思路就是0排头和1排头各算一次选最小的
每轮轮的时候，碰到这轮要加的，就累加非它的count，要不就累加个数
if n == 0:
	swap0 += count1
else:
	count1 += 1

if n == 1:
	swap1 += count0
else:
	count0 += 1

return min(swap1, swap0)