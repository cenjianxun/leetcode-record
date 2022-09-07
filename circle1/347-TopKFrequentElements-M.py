'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
'''
慢 faster than 31.75% of Python3
'''
'''
统计个数，用hashmap
'''
def topKFrequent(nums: List[int], k: int) -> List[int]:
    dic = {}
    for n in nums:
        if not n in dic:
            dic[n] = 1
        else:
            dic[n] = dic[n] + 1
    klist = sorted(list(dic.values()), reverse=True)[:k]
    result = []
    for key,value in dic.items():
        if value in klist:
            result.append(key)
    return result