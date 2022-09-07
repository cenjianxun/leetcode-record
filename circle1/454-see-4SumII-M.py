'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''

'''
可以把两两合并
'''

def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    dic = {}
    for a in nums1:
        for b in nums2:
            dic[a+b] = dic.get(a+b, 0) + 1
    res = 0
    for c in nums3:
        for d in nums4:
            if -(c+d) in dic:
                res = res + dic[-c-d]
    return res


# 优化：
def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    sums = collections.Counter(c+d for c in C for d in D)
    return sum(sums.get(-(a+b), 0) for a in A for b in B)