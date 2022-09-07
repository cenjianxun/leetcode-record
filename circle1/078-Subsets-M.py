'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

'''
这道题的坑就是list里的list需要独立出来，如果浅copy就不行
'''

# faster than 52.43% of Python3
# less than 93.72% of Python3
def addSub(preL, n):
    result = []
    for r in preL:
        temp = r[:]
        temp.append(n)
        result.append(temp)
    result.extend(preL)
    return result
    
def subsets(nums):
    result = [[]]
    for n in nums:
        result = addSub(result, n)
    return result

r = subsets([1,2,3])
print(r)


'''
小技巧：
helper(path):
    xxxx
    helper(path + [123])

相当于

helper():
    xxxx
    path.append(123)
    helper(path)
    path.pop()
'''