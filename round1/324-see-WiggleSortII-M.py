'''
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.
'''

'''
排序后 要倒着交叉
可以提高速度
'''

def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = sorted(nums)
    i = 0
    
    k = int((len(nums)-1)/2)
    j = k
    while i < len(nums):
        nums[i] = l[j]
        i = i + 2
        j = j - 1
        # print(nums, l[j])
    i = 1
    j = len(nums) - 1
    while i < len(nums):
        nums[i] = l[j]
        i = i + 2
        j = j - 1


'''
先对数组排序，然后找到中位数，用两个pt 从前半段和后半段的末尾交替取数。为什么要这么做呢？对于非重复序列来讲，这只是众多选择中的一种。从下面代码中的例子来看，wiggle1是用这种方法，由两个交替单调递减序列构成。wiggle2由一个单减一个单增构成，这两种都满足题意。但是注意到我们的目的只是让每个数字比它临近的两个数大/小就行了，这里大数被“浪费”在了波动末尾的较小值上。而如果数组中有重复数字，这个方法可能造成前面的波动不够大。比如第二个例子。由于这道题保证了一定有解，那么最保险的做法必须是用大数和大数去比较，才有可能找到解。
// nums    [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
// wiggle1 [2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 1, 2, 1, 2]
// wiggle2 [2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 3, 1, 3, 1]
————————————————

and 为什么要倒着插入呢: [4, 5, 5, 6]
因为先小后大，且交汇在中间，小的末尾和大的开头交汇，可能出现小的末尾和大的开头波动过小
'''
def wiggleSort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    mid = (len(nums) + 1) // 2 
    small, large = nums[:mid], nums[mid:]
    nums[::2] = small[::-1]
    nums[1::2] = large[::-1]
 

def wiggleSort(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    sort_nums = sorted(nums)
    L = len(nums)
    i, j, mid = 0, L - 1, L//2  
    print(mid, sort_nums)
    while j >= mid:
        nums[i] = sort_nums[j-mid]
        if i+1 < L:
            nums[i+1] = sort_nums[j]
        i += 2
        j -= 1