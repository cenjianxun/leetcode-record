'''
769. Max Chunks To Make Sorted
Medium

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

	Input: arr = [4,3,2,1,0]
	Output: 1
	Explanation:
	Splitting into two or more chunks will not return the required result.
	For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

	Input: arr = [1,0,2,3,4]
	Output: 4
	Explanation:
	We can split into two chunks, such as [1, 0], [2, 3, 4].
	However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
 
Constraints:

	n == arr.length
	1 <= n <= 10
	0 <= arr[i] < n
	All the elements of arr are unique.
'''

'''
不会

观察规律，4出现在第0位，意味着第0位到最后一位必须作为一组了，不然无法满足条件。同理，0出现在第n-1位，那么意味着第0到第n-1位必须作为一组。这两种考虑是等价的。

假设就从元素最终所在的位置的左侧进行考虑：4出现在第0位，不考虑后面3，2，1，0的位置，由于4最终一定出现在下标为4的位置，所以对于4的分组一定会包含3，也就是3的考虑被4的情况给覆盖了。

所以，此题又可以与区间问题关联起来，例如串3，4，0，1，2。我们看第一个3的时候，对3的理解变为它的覆盖范围是下标区间[0, 3]，也就是{3,4,0,1}。而后面4的作用范围是[1, 4]。我们发现两个下标区间是重叠的，对于最终答案，我们发现结果是1，也就是意味着此题转化为求[0, n -1]会出现多少个独立的小区间,和大楼轮廓问题有一些相似之处，可以覆盖的范围就是高度。

所以，此题的一种解法就是扫描，记录当前元素的从当前下标开始的区间的覆盖范围的当前最大值，（1）如果扫描下标比当前最大值小，意味着当前下标是被最大值所在区间给覆盖住的，也就不计入结果。（2）会不会出现当前下标大于最大值呢？也就是说最大值覆盖不到当前下标呢？不存在的，即使严格按照升序来排也做不到。（3）当前下标等于最大值，意味着之前最大值的覆盖范围在此处消失，此时对结果数加1，也就是说之前的区间是一个独立的区间。 最大值进行更新意味着什么？如果之前最大值覆盖范围已经消失，意味着新区间的开始，如果之前最大值覆盖范围还没有消失，意味着出现区间重叠（此时区间数不变），也就好比是一个楼被后面的高楼给覆盖了。
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = cur_max = 0
        for i, n in enumerate(arr):
            cur_max = max(cur_max, n)
            if cur_max == i:
                res += 1
        return  res