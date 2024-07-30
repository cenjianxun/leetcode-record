'''
659. Split Array into Consecutive Subsequences
Medium

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:

	Input: nums = [1,2,3,3,4,5]
	Output: true
	Explanation: nums can be split into the following subsequences:
	[1,2,3,3,4,5] --> 1, 2, 3
	[1,2,3,3,4,5] --> 3, 4, 5

Example 2:

	Input: nums = [1,2,3,3,4,4,5,5]
	Output: true
	Explanation: nums can be split into the following subsequences:
	[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
	[1,2,3,3,4,4,5,5] --> 3, 4, 5

Example 3:

	Input: nums = [1,2,3,4,4,5]
	Output: false
	Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more. 

Constraints:

	1 <= nums.length <= 104
	-1000 <= nums[i] <= 1000
	nums is sorted in non-decreasing order.
'''

'''
如何判断：
优先和前序列合并，再开辟新序列
但是[1,2,3,3,4,5] 不是12345和3，往后找
1233445 123 345
是优先组合3张的，后面的数n，如果发现n-1是一个end，就续在后面，是往前找。
如果n-1不是end，就开辟新顺子，必须保证n+1, n+2存在。
如果这个情况还不存在，就false

如何存储：
所以需要一个map存储每个数的freq，还有一个存每个顺子的tail
'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        end = collections.Counter()
        
        # 访问nums中的各个元素
        for num in nums:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif freq[num + 1] != 0 and freq[num + 2] != 0:
                # 查找后面两个元素拼凑出一个合法序列
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False 
        return True