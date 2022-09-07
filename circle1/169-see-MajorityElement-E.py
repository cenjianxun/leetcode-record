'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

'''
太蠢
'''
def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[int((len(nums)-1)/2)]

'''
其他方法：
1. 计数
2. 每次都找出一对不同的元素，从数组中删掉，直到数组为空或只有一种元素。 不难证明，如果存在元素e出现频率超过半数，那么数组中最后剩下的就只有e
'''