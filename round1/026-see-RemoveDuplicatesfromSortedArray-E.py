'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''


def removeDuplicates(nums):
    if not nums:
        return 0 
    if len(nums) == 1:
        return 1
    i = 0
    j = i + 1
    while j < len(nums):
        while j < len(nums) and nums[i] == nums[j]:
            print(i, j)
            j = j + 1
        i = i+1
        if j < len(nums):
            nums[i] = nums[j]
        # print(i, nums)
    return i 
nums = [0,0,0,1,1,1,2,2,2,2,2,2,3,3,4]
removeDuplicates(nums)

'''
呃我觉得第一次的方法比较好
下面这个在里面return left 外面return right 有点迷惑
'''
def removeDuplicates(self, nums: List[int]) -> int:
    left, right = 0, 1
    while right < len(nums):

        if nums[left] == nums[right]:
            temp = nums[right]
            left, right = left + 1, right + 1
            while right < len(nums) and temp == nums[right]:
                right = right + 1
            if right >= len(nums):
                print('in', left)
                return  left 
            nums[left] = nums[right]
        else:
            left, right = left + 1, right + 1
    # print('out', left)
    return right