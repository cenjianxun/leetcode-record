'''
Find the total sum of imbalance of all such groups.

 Given an array ranks of ranks of students in a school. All students need to be split into groups k. Find the total 'imbalance' of all groups. An imabalance of a group can be found as :
Sorting each group in the order of their ranks.
A group contributes to imbalance if any 2 students in the sorted array have a rank difference of more than 1.
Find the total sum of imbalance of all such groups.
This is the example that was given :
[4,1,3,2]
[1] contributes 0 to imbalance
[2] contributes 0 to imbalance
[3] contributes 0 to imbalance
[4] contributes 0 to imbalance
[‍‍‌‍‍4,1] contributes 1 to imbalance
[1,3] contributes 1 to imbalance
[3,2] contributes 0 to imbalance
[4,1,3] contributes 1 to imbalance
[1,3,2] contributes 0 to imbalance
[4,1,3,2] contributes 1 to imbalance
Answer = 1 + 1 + 1 = 3
'''

def totalSumOfImbalance(nums):
	res = 0
	for i in range(len(nums)-1):
		group = set()
		count = 0
		for j in range(i, len(nums)):
			count += 1
			if nums[j] - 1 in group:
				count -= 1
			if nums[j] + 1 in group:
				count -= 1
			if count > 1:
				res += 1
			group.add(nums[j])
	print(res)
	return res

nums = [4,1,3,2]
totalSumOfImbalance(nums)