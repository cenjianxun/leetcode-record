'''
1004. Max Consecutive Ones III
Medium

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

	Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
	Output: 6
	Explanation: [1,1,1,0,0,1,1,1,1,1,1]
	Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

	Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
	Output: 10
	Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
	Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
	 
Constraints:

	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
	0 <= k <= nums.length
'''

'''
例外情况太多了！
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
        res = 0
        i, j = 0, k-1
        if j >= len(zero) or not zero:
            return len(nums)
        if k == 0:
            for i in range(1, len(zero)):
                res = max(res, zero[i] - zero[i-1]-1)
            res = max(res, zero[0], len(nums)-zero[-1]-1)
            return res
        while i < len(zero) and j < len(zero):
            left, right = zero[i], zero[j] + 1
            print(i, j,left, right)
            while left > 0 and nums[left-1] == 1:
                left -= 1
            while right < len(nums) and nums[right] == 1:
                right += 1
            res = max(res, right-left)
            print(i, j, left, right, res)
            i, j = i+1, j+1
        return res

'''
滑动窗口：https://leetcode.cn/problems/max-consecutive-ones-iii/solution/jidao-by-iamysw-bs2s/

总结：用变量、哈希表或有序集合来记录当前窗口内的信息，如果窗口右端加入新元素后不满足要求则移除窗口左端的元素，左端口向前移动一步，同时更新变量、哈希表或有序集合。这个过程可以看出如果当前窗口不满足要求则左端口和右端口同时向前移动，且窗口大小保持不变，如果后续遇到了能满足要求的更大的窗口则左端口就停止移动，最后得到的窗口大小即是满足题目要求最大的窗口大小。

另外，这个方法能行得通的前提是：右端口开始移动时满足题目条件，但当右端口移动到某个位置之后不满足题目条件，且此时右端口就算继续向前移动也不能使窗口内满足条件。比如下面这道题就不能用这个方法：525. 连续数组，因为不满足上诉前提。
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        count = 0
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            right += 1
            print(nums[left:right+1])
        return right - left

'''
普通：
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        count = 0
        res = 0
        while j < len(nums):
            if nums[j] != 1:
                count += 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res