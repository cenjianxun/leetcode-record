'''
330. Patching Array
Hard

Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

Example 1:

	Input: nums = [1,3], n = 6
	Output: 1
	Explanation:
	Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
	Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
	Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
	So we only need 1 patch.

Example 2:

	Input: nums = [1,5,10], n = 20
	Output: 2
	Explanation: The two patches can be [2, 4].

Example 3:

	Input: nums = [1,2,2], n = 5
	Output: 0
 
Constraints:

	1 <= nums.length <= 1000
	1 <= nums[i] <= 104
	nums is sorted in ascending order.
	1 <= n <= 231 - 1
'''

'''
本来范围为[1,total]，如果添加一个数num，范围会变成[1, total]U[num, total+num]
如果 total 和 num 挨着或有交集，范围就是[1, total+num]
否则，需要添加的数是 total+1，构成新范围[1，total*2+1]，再来比较 total*2+1和num的大小
'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        right = 0
        res = 0
        i = 0
        while right < n:

            if i < len(nums) and right + 1 >= nums[i]:
                right = right + nums[i]
                i += 1
            else:
                res += 1
                right = right + right + 1
        return res