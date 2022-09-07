'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

'''
1. range的第三个参数为-1的话 第一个参数要比第二个大！！！
2. k > len(nums)的情况
'''
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    while len(nums) <= k:
        k = k - len(nums)
    temp = []
    for i in range(len(nums)-k, len(nums)):
        temp.append(nums[i])
    for i in range(len(nums)-k-1, -1, -1):
        nums[i+k] = nums[i]
        # print(i, nums[i+k], nums[i])
    for i in range(0, k):
        nums[i] = temp[i]

'''
1. 特么 k = k%len(nums) !!表示实际挪的！
2. 后面+前面
3. 原地赋值需要 nums[:] = 
'''
def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k%len(nums)
    nums[:] = nums[-k:] + nums[:-k]