'''
435. Non-overlapping Intervals
Medium

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

	Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
	Output: 1
	Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

	Input: intervals = [[1,2],[1,2],[1,2]]
	Output: 2
	Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

	Input: intervals = [[1,2],[2,3]]
	Output: 0
	Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

	1 <= intervals.length <= 105
	intervals[i].length == 2
	-5 * 104 <= starti < endi <= 5 * 104
'''

'''
超时
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        L, needs = len(intervals), 0
        def findend(nums):
            end = nums[0][1]
            for n in nums:
                end = min(n[1], end)
            return end
        while intervals:
            end = findend(intervals)
            rest = []
            for p in intervals:
                if p[0] >= end:
                    rest.append(p)
            intervals = rest
            needs += 1
        
        return L - needs

'''
只要重叠就+1
只在重叠的情况下，把右边end改短
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                ans += 1
                if intervals[i][1] > intervals[i-1][1]:
                    intervals[i] = intervals[i-1]
        return ans