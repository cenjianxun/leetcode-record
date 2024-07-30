'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.'''

'''
错误方法↓
1. python会偷懒 看别的方法
2. 小细节 % 和 int 等
'''
# faster than 23.26% of Python3 
def findMedianSortedArrays(nums1, nums2):
    num = sorted(nums1 + nums2)
    lens = len(num)/2
    if len(num)%2:
        return  num[int(lens)]
    else:
        return (num[int(lens)-1] + num[int(lens)])/2

'''
直接折半
'''
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
    n1,n2  = len(nums1), len(nums2)
    if n1 > n2:
        nums1, nums2, n1, n2 = nums2, nums1, n2, n1 #让nums2和n2更大

    imin, imax, half_len = 0, n1, (n1 + n2 + 1) // 2 #若为奇数，中位数算入half_len即左侧
    while imin <= imax: #二分查找的标准循环条件
        i = (imin + imax) // 2 #二分查找标准迭代条件.i为nums1分入左侧的个数
        j = half_len - i # j为nums2分入左侧的个数
        if j > 0 and i < n1 and nums1[i] < nums2[j-1]: # i太小
            imin = i + 1
        elif i > 0 and j < n2 and nums1[i-1] > nums2[j]: # i太大
            imax = i - 1
        else:
            # 结果已经得出
            if i == 0: max_of_left = nums2[j-1] #所有的nums1大于nums2
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])

            if (n1 + n2) % 2 == 1: #如果总数为奇数 中位数在half_len末尾即左侧末尾
                return max_of_left

            if i == n1: min_of_right = nums2[j]
            elif j == n2: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

'''
首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，而A中的第3个数A[2]=5；B中的第3个数B[2]=6；而A[2]<B[2]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1]这四个数，也就是说A[2]最多可能是第5个大的数，由于我们要求的是getKth(A, B, 7)；现在就变成了求getKth(A', B, 4)；即A' = {7}；B不变，求这两个数列的第4个小的数，因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。

改编版↓
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        lens = len(nums1) + len(nums2) 
        if lens%2:
            return self.getKth(nums1, nums2, lens//2)
        else:
            return (self.getKth(nums1, nums2, lens//2 - 1) + self.getKth(nums1, nums2, lens//2))/2
        
        
    def getKth(self, n1, n2, k):
        k = int(k)
        if len(n1) > len(n2):
            n1, n2 = n2, n1
        print(n1, n2, k)
        if not n1:
            return n2[k]
        if k == len(n1) + len(n2) - 1:
            return max(n1[-1], n2[-1])
        i1 = len(n1)//2
        i2 = int(k - i1)
        if n1[i1] > n2[i2]:
            return self.getKth(n1[:i1], n2[i2:], i1)
        else:
            return self.getKth(n1[i1:], n2[:i2], i2)



def findMedianSortedArrays(self, nums1, nums2):
    l = len(nums1) + len(nums2)
    if l % 2:  # the length is odd
        return self.findKthSmallest(nums1, nums2, l//2+1)
    else:
        return (self.findKthSmallest(nums1, nums2, l//2) +
        self.findKthSmallest(nums1, nums2, l//2+1))*0.5
    
def findKthSmallest(self, nums1, nums2, k):
    # force nums1 is not longer than nums2
    if len(nums1) > len(nums2):
        return self.findKthSmallest(nums2, nums1, k)
    if not nums1:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    pa = min(k/2, len(nums1)); pb = k-pa  # take care here
    if nums1[pa-1] <= nums2[pb-1]:
        return self.findKthSmallest(nums1[pa:], nums2, k-pa)
    else:
        return self.findKthSmallest(nums1, nums2[pb:], k-pb)