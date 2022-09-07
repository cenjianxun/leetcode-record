'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

'''
没做出来。好多方法。时间复杂度。
'''

def longestConsecutive( nums: List[int]) -> int:
    nums = set(nums)
    seq = 0
    for n in nums:
        if not n-1 in nums:
            i = 1
            while n+i in nums:
                i = i + 1
            seq = max(seq, i)
    return seq

'''
这个方法需要一个dic存，存的内容是当前数字的长度，更新的技巧是，，如果上一个or下一个存在，那么！！不是更新上一个or下一个，而是取上/下一个的值=上/下一个的长度，更新的是i+/- len，即边界的数的长度
'''
def longestConsecutive(self, nums: List[int]) -> int:
    d = {}
    ans = 0
    for i in nums:
        if i not in d:
            left = d.get(i-1, 0)
            right = d.get(i+1, 0)
            length = left + right + 1
            ans = max(ans, length)

            d[i] = length
            d[i-left] = length
            d[i+right] = length
            print(i, i-left, i+right, length)
            print(d)
    return ans