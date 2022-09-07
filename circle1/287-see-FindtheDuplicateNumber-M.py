'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''

'''
看看其他解法
'''

def findDuplicate(nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        temp = nums[0]
        nums[0] = nums[temp]
        nums[temp] = temp
        i = i + 1
        # print(nums)
    return nums[0]


'''
查环的解法，值为下一轮的index
如果有重复的数就说明有环 因为会出现多对一映射
找环的入口，使用快慢指针 https://www.cnblogs.com/zhangjiuding/p/10926157.html
'''
# faster than 79.36% of Python3

def findDuplicate(nums) -> int:
    # i = 0
    # while i < len(nums):
    #     temp = nums[0]
    #     nums[0] = nums[temp]
    #     nums[temp] = temp
    #     i = i + 1
    #     # print(nums)
    # return nums[0]
    # 如果只有两个元素，第一个元素一定是重复元素
    if len(nums) == 2:
        return nums[0]
    
    # fast每次走两步，slow每次走一步，起始点可以为任意位置
    # 此循环只证明有循环
    fast = 0
    slow = 0
    # python没有do while，所以在循环外写了一遍
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    # fast从起点每次走一步，一定会与slow相遇，此时slow可能在环中走了多倍的L步。
    # L为环一圈的步数
    fast = 0
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    return fast

# 没懂
def findDuplicate(nums: List[int]) -> int:
    l = 0
    r = len(nums)-1
    while l < r:
        mid = (r + l) // 2
        count = 0
        for n in nums:
            if n <= mid:
                count = count + 1
        if count <= mid:
            l = mid + 1 
        else:
            r = mid 
        print(l, r, mid)
    return r