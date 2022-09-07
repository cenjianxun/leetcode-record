'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
不能用除号！
'''

def productExceptSelf(nums):
    zero = [1,0]
    for n in nums:
        if n:
            zero[0] = zero[0] * n
        else:
            zero[1] = zero[1] + 1
    result = []
    if zero[1] == 0:
        for n in nums:
            result.append(int(zero[0]/n))
    elif zero[1] == 1:
        for n in nums:
            if n == 0:
                result.append(zero[0])
            else:
                result.append(0)
    else:
        for n in nums:
            result.append(0)
    return result


'''
维护两个左乘积和右乘积
可以用temp代替，不用数组
'''
def productExceptSelf(nums):
    res = [0] * len(nums)
    temp = 1
    for i in range(len(nums)):
        res[i] = temp
        temp = temp * nums[i]
    temp = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = temp * res[i]
        temp = temp * nums[i]
        
    return res