'''
321. Create Maximum Number
Hard

You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

Example 1:

    Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
    Output: [9,8,6,5,3]

Example 2:

    Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
    Output: [6,7,6,0,4]

Example 3:

    Input: nums1 = [3,9], nums2 = [8,9], k = 3
    Output: [9,8,9]
 
Constraints:

    m == nums1.length
    n == nums2.length
    1 <= m, n <= 500
    0 <= nums1[i], nums2[i] <= 9
    1 <= k <= m + n
'''

'''
遍历k分配给两个数组的情况
这里merge和比较用的是python自带的？
自己写见下：


❗❗❗要注意的是❗❗❗
传递参数传递的是数组，数组是可变的，在新函数里不能改这个数组！否则原数组会变
merge里不能用pop。
'''
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxNum = [0] * k
        for k1 in range(k + 1):
            k2 = k - k1
            if k1 <= len(nums1) and k2 <= len(nums2):
                maxnums1 = self.maxKNum(nums1, k1)
                maxnums2 = self.maxKNum(nums2, k2)
                curMaxNum = self.mergeMaxNum(maxnums1, maxnums2)
                maxNum = max(maxNum, curMaxNum)
                #print(k1, maxnums1, k2, maxnums2, curMaxNum, maxNum)
        return maxNum
    
    def mergeMaxNum(self, nums1, nums2):
        stack = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if nums1[i:] > nums2[j:]:
                stack.append(nums1[i])
                i += 1
            else:
                stack.append(nums2[j])
                j += 1
        return stack
    
    def maxKNum(self, nums, k):
        stack = []
        remove = len(nums) - k
        if remove == 0:
            return nums
        for n in nums:
            while stack and remove and stack[-1] < n:
                stack.pop()
                remove -= 1
            stack.append(n)
        while remove:
            stack.pop()
            remove -= 1
        return stack


'''
这类比较的伪代码：
先循环掉A和B开头相同的部分。

if（前面都相等）如果有一方循环完了：
    那么循环完的数字小
else 没循环完:
    当前数字大的数组大

so merge的时候，先用这个逻辑比较两个数组的大小（为了方便在merge的时候调用，上面的函数返回true和false
'''
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        maxNum = [0] * k
        for k1 in range(k + 1):
            k2 = k - k1
            #print(k1,len(nums1), k2, len(nums2))
            if k1 <= len(nums1) and k2 <= len(nums2):
                maxnums1 = self.maxKNum(nums1, k1)
                maxnums2 = self.maxKNum(nums2, k2)
                curMaxNum = self.mergeMaxNum(maxnums1, maxnums2)
                maxNum = maxNum if self.compareNum(maxNum, 0,curMaxNum,0) else curMaxNum
                #print(k1, maxnums1, k2, maxnums2, curMaxNum, maxNum)
        return maxNum
    
    def compareNum(self, nums1, i, nums2, j):
        # nums1 > nums2, true
 
        while i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
            i, j = i + 1, j + 1
        if i == len(nums1):
            return False
        elif j == len(nums2):
            return True
        else:
            if nums1[i] > nums2[j]:
                return True
            else:
                return False
        
    def mergeMaxNum(self, nums1, nums2):
        stack = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if self.compareNum(nums1, i, nums2, j):
                stack.append(nums1[i])
                i += 1
            else:
                stack.append(nums2[j])
                j += 1
        return stack
    
    def maxKNum(self, nums, k):
        stack = []
        remove = len(nums) - k
        if remove == 0:
            return nums
        for n in nums:
            while stack and remove and stack[-1] < n:
                stack.pop()
                remove -= 1
            stack.append(n)
        while remove:
            stack.pop()
            remove -= 1
        return stack