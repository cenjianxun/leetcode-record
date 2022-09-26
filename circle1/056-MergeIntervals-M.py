'''
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
'''
警惕边界 最后还有一个temp
警惕题目中隐含的情况分类
'''

# faster than 75.97% of Python3
def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals = sorted(intervals, key=lambda x: x[0])
    i = 1
    temp = intervals[0]
    while i < len(intervals):
        print(i, temp, intervals[i])
        if temp[1] >= intervals[i][0]:
            temp = [temp[0], max(temp[1], intervals[i][1])]
        else:
            result.append(temp)

            temp = intervals[i]
        i = i + 1
    result.append(temp)
    return result


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        left, right = intervals[0]
        for start, end in intervals[1:]:
            if right < start:
                res.append((left, right))
                left, right = start, end
            else:
                left = min(left, start)
                right = max(right, end)
        res.append((left, right))
        return res