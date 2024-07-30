'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
'''
奇怪的解法
要注意 如果不存在 乘法不能返回1
'''

def maxProduct(nums: List[int]) -> int:
    neg = []
    zero = []
    for i in range(0, len(nums)):
        if nums[i] == 0:
            zero.append(i)
        if nums[i] < 0:
            neg.append(i)
    result = [max(nums)]
    start = 0
    zero.append(len(nums))
    
    def product(L):
        if not L:
            return -100000
        result = 1
        for l in L:
            result = result * l
        return result
    
    for i in zero:
        temp = []
        while neg and neg[0] < i:
            temp.append(neg.pop(0))
        if len(temp)%2:
            print(i, temp, nums[start:temp[-1]])
            result.append(max(product(nums[start:temp[-1]]), product(nums[temp[0]+1:i])))
        else:
            result.append(product(nums[start:i]))
        start = i + 1
        # print(result)
    return max(result)


'''
连乘比连加多存一个最小值，因为负号会把最大值变成最小值

当前的min和max必须是前一个的最大最小值*当前值，&& +比较当前值本身
先比较出来，然后把它俩当成下一轮的preMax/Min
'''
def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 
    preMin = preMax = res = nums[0]
    for i in range(1, len(nums)):
        Min = min(preMin * nums[i], nums[i], preMax * nums[i])
        Max = max(preMin * nums[i], nums[i], preMax * nums[i])
        res = max(Max, res) 
        preMin, preMax = Min, Max
    return res

'''
220615

暴力超时
'''
def maxProduct(self, nums: List[int]) -> int:
    res = float('-inf')
    for i in range(len(nums)):
        temp = 1
        for j in range(i, len(nums)):
            temp = temp * nums[j]
            res = max(res, temp)
            #print(i, j, temp)
    return res