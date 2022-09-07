'''
164. Maximum Gap
Hard

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

	Input: nums = [3,6,9,1]
	Output: 3
	Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

	Input: nums = [10]
	Output: 0
	Explanation: The array contains less than 2 elements, therefore return 0.
 
Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''

'''
不会

桶：
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        #nums = set(nums)
        if len(nums) < 2:
            return 0
        
        max_num, min_num = max(nums), min(nums)
        bucket_width = max(1, (max_num - min_num)//(len(nums) - 1))
        buckets = [[] for _ in range((max_num - min_num)//bucket_width + 1)]
        
        for i in range(len(nums)):
            loc = (nums[i] - min_num) // bucket_width
            buckets[loc].append(nums[i])
        
        prev_max = float('inf')
        max_gap = 0
        for i in range(len(buckets)):
            if buckets[i]:
                if prev_max != float('inf'):
                    max_gap = max(max_gap, min(buckets[i]) - prev_max)
                prev_max = max(buckets[i])
        return max_gap

'''
基数
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        bit, max_bit = 0, len(str(max(nums)))
        while bit < max_bit:
            buckets = [[] for _ in range(10)]
            for num in nums:
                buckets[(num//10**bit) % 10].append(num)
            nums.clear()
            for num_list in buckets:
                nums.extend(num_list)
            bit += 1
        return max(nums[i] - nums[i-1] for i in range(1, len(nums)))
