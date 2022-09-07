'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
'''

'''
一边查找一边排序
'''
import bisect
def countSmaller(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    ans = []
    for i in range(len(nums)-1, -1, -1):
        n = bisect.bisect_left(ans, nums[i])
        result[i] = n
        ans.insert(n, nums[i])
        # print(nums[i], n, ans)
    return result


'''
带index的元组对的list：sort(list(enumerate(nums)))
'''
def countSmaller(nums):
    def sort(enum):
        # print('b', enum)
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            # print(left, right)
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        # print('a', enum, smaller)
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

'''
220618
超时

基本思想就是i右边的还是要排序，排序快的就是归并排序
'''
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    res[i] = res[i] + 1
        return res