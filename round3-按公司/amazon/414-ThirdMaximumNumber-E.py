'''
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?

'''

def thirdMaximumNumber(nums):
	stack_a, stack_b = [], []
	for n in nums:
		while stack_a and stack_a[-1] <= n:
			not_bigger = stack_a.pop()
			if not_bigger != n:
				stack_b.append(not_bigger)
		stack_a.append(n)
		while len(stack_a) < 3 and stack_b:
			stack_a.append(stack_b.pop())
		# print(stack_a)
		# print(stack_b)
	if len(stack_a) < 3:
		return stack_a[0]
	else:
		return stack_a[2]

nums = [2,2,3,1]
res = thirdMaximumNumber(nums)
print(res)

'''
这题快的诀窍就是，找的位次是恒定的，可以设恒定的变量占坑，这样就变成了常数时间。
'''

