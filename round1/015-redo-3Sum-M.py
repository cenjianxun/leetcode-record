'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

'''
时间复杂度 三个做法:固定一个【固定means遍历它】 其他两个夹逼

'''

def test15(nums):
    n = sorted(nums)
    result = []
    # print(n)
    for i in range(0, len(n)-2):
        j = i + 1
        k = len(n) - 1      
        if n[i] > 0:
            break
        else:
            while k > j :
                target = [n[i], n[j], n[k]]
                # print(n[i],n[j],n[k])
                if sum(target) < 0:
                    j = j + 1
                if sum(target) > 0:
                    k = k - 1
                if sum(target) == 0:
                    if not target in result:
                        result.append(target)
                    while n[j] == target[1] and k > j:
                        # print(j, n[j])
                        j = j + 1
                    while n[k] == target[2] and k > j:
                        # print(k, n[k])
                        k = k - 1
            while n[i] == target[0] and i<len(n)-2 :
                i = i + 1
    return result


'''
两边夹逼的灵魂在于：
同一个状态既可以往右走，又可以往左走，这样起码可以省下一半时间。
而这个场景，恰巧又可以判断往哪边走。如果值大了，就往小调整，如果值小了，就往大调整。

and 这个题容易超时的地方，就是可能有很多的重复值。
不能直接消掉，因为有时又需要，两个重复值可以构成一个可能解。
那么就是 在其他两个值不动时，这个值可以排除重复，while给它循环掉。
'''
def threeSum(nums: List[int]) -> List[List[int]]:
    res = set()
    
    if len(nums) < 3:
        return res
    nums.sort()
    i = 0
    print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            target = (nums[i], nums[j], nums[k])
            # print(i,j,k,target)
            if sum(target) == 0:
                if not target in res:
                    res.add(target)
                j = j + 1
                k = k - 1
                while j < k and nums[j] == target[1] and nums[k] == target[2]:
                    j = j + 1
            elif sum(target) > 0:
                k = k - 1
                while nums[k] == target[2] and j < k:
                    k = k - 1
            else:
                j = j + 1
                while nums[j] == target[1] and j < k:
                    j = j + 1

        while i < len(nums) - 2 and nums[i - 1] == nums[i]:
            i = i + 1
    return res


'''
22.5.29
左边固定意思是遍历
有while k<j之后：
1.时刻保持k<j
2.里面一次走一步就好了，左+右-是并列在while里的（所以快）
3.当命中之后要记得第二个该移的左+一次
超时重复：
1.i时一次
2.里面命中时一次
3.也是比较前一个就行了，用while
'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    res = set()
    if len(nums) < 3:
        return  res
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        k, j = i + 1, len(nums) - 1
        while k < j:
            if k < j and nums[i] + nums[j] + nums[k] > 0:
                j = j - 1
            if k < j and nums[i] + nums[j] + nums[k] < 0:
                k = k + 1
            if k < j and nums[i] + nums[j] + nums[k] == 0:
                res.add((nums[i], nums[k], nums[j]))
                k = k + 1
                while k < j and nums[k] == nums[k - 1]:
                    k = k + 1
                while k < j and nums[j] == nums[j - 1]:
                    j = j - 1
    return res

'''
220703
在固定左位，j和k遍历中间靠的时候，剪枝的地方：如果和前一个数字相等，略过。如果最小值都>0了，跳出
注意！这道题res.append之后jk还是要继续前进！所以大if分两支就行了
'''
# faster than 36.05% of Python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            while j < k and nums[k] >= 0:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1   
                else:
                    if sum3 == 0:
                        res.add((nums[i],nums[j],nums[k]))
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1 
        return res
'''
分享一个快的：
如果第二个数不在set里，就把前两个数的负值放进set
如果在往后遍历发现一个值在set里，说明是答案
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)