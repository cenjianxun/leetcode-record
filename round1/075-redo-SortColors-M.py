'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''

'''
1. 计数排序
2. 中间的选中间，左边一定比它小，右边一定比它大
'''


def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    store = [0] * 3
    for i in range(len(nums)):
        store[nums[i]] = store[nums[i]] +1
    print(store)
    j = 0
    for i in range(len(nums)):
        while not store[j]: #！！！！！！！！！！！！！！！
            j = j + 1
        nums[i] = j
        store[j] = store[j] - 1

'''
redo的意思是需要：一看到这道题就要想到快排。
快排：选一个数，比它小的都放它左边，比它大的都放它右边
因为只有三种情况，所以就分三种情况。 三个指针，left，cur，right。 cur就分三种情况
'''



def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = cur = 0
    right = len(nums) - 1
    while cur <= right:
        # print(left, cur, right, nums)
        if nums[cur] == 0:
            nums[cur], nums[left] = nums[left], nums[cur]
            left = left + 1
            cur = cur + 1
        elif nums[cur] == 1:
            cur = cur + 1
        else:
            nums[cur], nums[right] = nums[right], nums[cur]
            right = right - 1



'''
220610
redo的意思是：follow up：
① 只能遍历一次
② 如果有k种颜色怎么办：
'''
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 3
    color_min, color_max = 0, k - 1
    left, right = 0, len(nums) - 1
    i = 0
    while color_min < color_max:
        while i <= right:
            if nums[i] == color_min:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == color_max:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        color_min += 1
        color_max -= 1
        i = left