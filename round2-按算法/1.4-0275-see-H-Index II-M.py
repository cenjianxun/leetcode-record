'''
275. H-Index II
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

You must write an algorithm that runs in logarithmic time.

Example 1:

	Input: citations = [0,1,3,5,6]
	Output: 3
	Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
	Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
	Example 2:

	Input: citations = [1,2,100]
	Output: 2

Constraints:

	n == citations.length
	1 <= n <= 105
	0 <= citations[i] <= 1000
	citations is sorted in ascending order.
'''

'''
即：找到最后一个index，满足citations[index] >= len - index

如果用start < end 就会出错
此时需要用 mid = (start + end + 1)//2
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations) 
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            h = N - mid
            if citations[mid] >= h:
                end = mid - 1
            else:
                start = mid + 1
        return N - start

'''
[10 10 10 20 20 20 30 30]
lowerBound: 
找第一个>= 20的
本题：找最后一个>=20的

upperBound：
找第一个>20的

二分查找下标 or 答案，我们主要分析答案每次的所在区间，根据 check 函数来决策如何缩小答案区间，
因此，只需要记住 upperBound 和 lowerBound 两个二分方式即可。

若二分答案是求最小满足值，我们可以直接使用 lowerBound。

答案的分布区间为：【不满足，最大不满足，最小满足，满足】
假定答案区间为：[0, n]
那么，每次 check 函数后，若满足，则 right = mid，因为最佳答案一定在 [0, mid] 中，
反之为 [mid + 1, right]

最终答案：left == right 返回二者其一都可

若二分答案是求最大满足值，我们可以转变思维，变为求最小不满足值，最后的答案减一即可。
答案的分布区间为：【满足，最大满足，最小不满足，不满足】，此时依然可以使用 lowerBound 求第一个最小不满足值，其前一位即为原本的答案。

原答案范围：[0, n]
转变后：[1, n + 1]
答案：(left or right) - 1

而 upperBound 是用于求第一个大于 x 的下标，按需使用即可。
'''