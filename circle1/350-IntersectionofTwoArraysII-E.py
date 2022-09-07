'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

'''
可以用collections.Counter
遍历第二个的时候可以减值
'''
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # faster than 27.76% of Python3
    nums1, nums2 = (nums1,nums2) if len(nums1) < len(nums2) else (nums2,nums1)
    result = []
    for n in nums1:
        if n in nums2:
            result.append(n)
            nums2.remove(n)
    return result

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # faster than 68.48% of Python3 
    dic1 = {}
    for n in nums1:
        if not n in dic1:
            dic1[n] = 1
        else:
            dic1[n] = dic1[n] + 1
    dic2 = {}
    for n in nums2:
        if not n in dic2:
            dic2[n] = 1
        else:
            dic2[n] = dic2[n] + 1
    inter = set(list(dic1.keys())) & set(list(dic2.keys()))
    print(inter, dic1,dic2)
    result = []
    for i in inter:
        n = min(dic1[i], dic2[i])
        result.extend([i] * n)
    return result