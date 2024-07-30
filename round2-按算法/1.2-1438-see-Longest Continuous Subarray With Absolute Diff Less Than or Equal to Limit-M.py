'''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

    Input: nums = [8,2,4,7], limit = 4
    Output: 2 
    Explanation: All subarrays are: 
    [8] with maximum absolute diff |8-8| = 0 <= 4.
    [8,2] with maximum absolute diff |8-2| = 6 > 4. 
    [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
    [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
    [2] with maximum absolute diff |2-2| = 0 <= 4.
    [2,4] with maximum absolute diff |2-4| = 2 <= 4.
    [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
    [4] with maximum absolute diff |4-4| = 0 <= 4.
    [4,7] with maximum absolute diff |4-7| = 3 <= 4.
    [7] with maximum absolute diff |7-7| = 0 <= 4. 
    Therefore, the size of the longest subarray is 2.

Example 2:

    Input: nums = [10,1,2,4,7,2], limit = 5
    Output: 4 
    Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

    Input: nums = [4,2,2,2,4,4,2,2], limit = 0
    Output: 3

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    0 <= limit <= 109
'''

'''
4. 如果stack里存的是nums的index，注意外面套nums。 1438
5. while最后注意+1
'''
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        minStack, maxStack = [], []
        i = j = 0
        while j < len(nums):
            while minStack and nums[minStack[-1]] > nums[j]:
                minStack.pop()
            while maxStack and nums[maxStack[-1]] < nums[j]:
                maxStack.pop()   
            minStack.append(j)
            maxStack.append(j)
            while nums[maxStack[0]] - nums[minStack[0]] > limit:
                i += 1
                while maxStack[0] < i:
                    maxStack.pop(0)
                while minStack[0] < i:
                    minStack.pop(0)
            res = max(res, j - i + 1)
            j = j + 1
            #print(i,j,minStack,maxStack,res)
        return res