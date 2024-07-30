'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''
 
def twoSum_force(nums, target):
    m = 0
    n = len(nums) - 1
    while nums[m] + nums[n] != target:
        n = n - 1
        if m == n:
            m = m + 1
            n = len(nums) - 1
    return [m, n]
    

'''
补：
上面这个方法实际上还是N^2的复杂度。包括一层for循环里带 nums[i] in nums 判断的，因为in的复杂度是O(n)。

要降低一维的复杂度，只能用空间换时间的方式，在判断in不in的步骤使用O(1)做到，因此只能用dic实现。
但是dic实现的方式要注意一个问题：此题规定了一个值只能用一次，所以要额外判断sub（=target-nums[i]）是否取到了同一个值。
因此有个改进方法是，将取过的值放进一个栈里。

'''

def twoSum(nums, target):
    dic = {}
    for i, v in enumerate(nums):
        sub = target - v
        if sub not in dic:
            dic[v] = i
        else:
            return [i, dic[sub]]

    
nums = [2,7,11,15]
target = 9
res = twoSum(nums, target)
print(res)

