'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

'''
这个动态规划真的是
'''

def maxSubArray(nums):
    preSums = nums[0]
    sums =  nums[0]
    for i in range(1, len(nums)):
        # print(preSums, nums[i])
        preSums = nums[i] if preSums < 0 else preSums+nums[i]
        sums = max(sums, preSums)
 
    return sums
         
nums = [-2,1,-3,4,-1,2,1,-5,4]
r = maxSubArray(nums)
print(r)


'''
原本的动态规划是这样子的
为什么要用动态规划：
因为全局的值，需要在每一步的最优选里挑出全局最优选
为什么不能直接挑出全局的值， 因为全局的值不能在途中确定【方向】，
直接的方法，中途虽然没有解，但是确定解的方向。
但是ep：[6，-3，（）]
最终的最大值此时是不确定的，如果第三个值是4，最大值就是新的，如果第三个值是1，最大值就仍然是6：：：所以需要把每一步的解都记下来。

改进就是：
因为记下来的值只用1次，所以可以把记录的list改成str，每一步都再求一次max
改进的动态规划总是需要两个记录串，一个记最终的结果，一个记当前的结果（list->temp)

=====
分解成子问题：以nums[i]结尾的串最大值是多少。
所以以nums[i]结尾的，需要nums[i-1]结尾的最大值的结果
dp[i]=max{nums[i],dp[i−1]+nums[i]} ==> 状态转移方程
'''
def maxSubArray(nums: List[int]) -> int:
    dp = [nums[0]]
    for i in range(1, len(nums)):
        if dp[i-1] < 0:
            dp.append(nums[i])
        else:
            dp.append(dp[i-1]+nums[i])        
    return max(dp)