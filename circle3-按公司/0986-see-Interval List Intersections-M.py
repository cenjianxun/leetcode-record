'''
986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

	Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
	Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
	Example 2:

	Input: firstList = [[1,3],[5,9]], secondList = []
	Output: []

Constraints:

	0 <= firstList.length, secondList.length <= 1000
	firstList.length + secondList.length >= 1
	0 <= starti < endi <= 109
	endi < starti+1
	0 <= startj < endj <= 109
	endj < startj+1
'''

'''
注意下一轮弹出哪个
'''
class Solution:
    def intervalIntersection(self, alist: List[List[int]], blist: List[List[int]]) -> List[List[int]]:
        res = []
        if not alist or not blist:
            return res
        
        a, b = alist.pop(0), blist.pop(0)
        while a and b:
            if a[0] < b[0]:
                if a[1] < b[0]:
                    a = alist and alist.pop(0) or ''
                else:
                    res.append((b[0], min(a[1], b[1])))
                    if a[1] < b[1]:
                        a = alist and alist.pop(0) or ''
                    else:
                        b = blist and blist.pop(0) or ''
            else:
                if a[0] > b[1]:
                    b = blist and blist.pop(0) or ''
                else:
                    res.append((a[0], min(a[1], b[1])))
                    if a[1] < b[1]:
                        a = alist and alist.pop(0) or ''
                    else:
                        b = blist and blist.pop(0) or ''              
        print(a, b)
        return res


'''
标准答案
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        if not A or not B:
            return res
        i = j = 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res