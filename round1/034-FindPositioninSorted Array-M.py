'''
34. Find First and Last Position of Element in Sorted Array
'''
'''
注意跳出的条件
'''

def searchRange(nums, target):
    if not nums or target < nums[0] or target > nums[-1]:
        return [-1, -1]
    result = [0, len(nums)-1]
    while result[1] > result[0]:
        mid = int((result[1] + result[0])/2)
        # print(result, mid)
        if mid in result:
            break
        if nums[mid] > target:
            result[1] = mid
        elif nums[mid] < target:
            result[0] = mid
        else:
            result = [mid, mid]
            while result[0] > 0 and nums[result[0] - 1] == target:
                result[0] = result[0] - 1
            while result[1] < len(nums) - 1 and nums[result[1] + 1] == target:
                result[1] = result[1] + 1
            break
    # print(result, nums[result[0]], nums[result[1]])
    if nums[result[0]] != target and nums[result[1]] != target:
        return [-1, -1]
    if nums[result[0]] == target and nums[result[1]] != target :
        return [result[0], result[0]]
    if nums[result[1]] == target and nums[result[0]] != target:
        return [result[1], result[1]]
    return result


result = searchRange([0,1], 0)
print(result)

'''
当我们使用传统二分查找思路找到和target相等的值的索引的时候，我们继续分头向前向后循环，直到找到不等于target的值

应该用一个helper，然后求left和right 分别调用，两次
'''