'''
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:

    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:

    Input: matrix = [[-5]], k = 1
    Output: -5
 
Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2
'''

'''
两种方法：① 堆 ② 【值】二分

前置知识：
用堆的情况：求第k，前k。求第k大用最小堆，第k小用最大堆。

值二分：也是求第k，前k。
方式：找出值的上限和下限。再找出中值，再缩减。同时统计搜索的数量，和k比较大小。
如果搜索到的数量是小于k的，那么M不够大；反之，M太大；最后，如果M缩减到一个点的时候（注意不存在提前返回），就可以说，M就是答案。
'''

'''
A. 用堆：
    有两种
    1. 将所有元素都过一遍堆，要剩下的顶是第k小，进去的就应该是负值，即大顶堆
    2. 先将所有元素进堆，再pop k个，第k个就是最小，这时候就是小顶堆
      -> 这种方式，如果能保证进去的都更小，就不用都进堆，那么需要一个queue，bfs找小的那些
      从左上开始向右下找

此方法时间复杂度是O(klogn)，其中k的范围是0到n^2，也就是说，最坏情况下， 时间复杂度是O(n^2 * logn)
'''
import heapq
from tools.heapq_showtree import show_tree

class Solution:
    # 第一种
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for i in range(len(matrix)):
            nums.extend(matrix[i])
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return nums[0]

    '''
    第二种。
    这样还是提前初始化好res，循环k次比较好。因为list里有不止一个值
    这里每一步push都要用heap的push

    要注意的是斜像右下找的时候，有可能进入重复值。
    所以规定只有每一行开始向下找，其余都向右找。 if j == 0 and i < m - 1：
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        res = None
        for _ in range(k):
            res, i, j = heapq.heappop(q)
            #print(res,i,j, n-1)
            if j == 0 and i < m - 1:
                heapq.heappush(q, (matrix[i+1][j], i+1, j))
            if j < n - 1:
                heapq.heappush(q, (matrix[i][j+1], i, j+1))
        return res


'''
B. 值二分
   首先找到值上下界，也就是矩阵的左上角和右下角分别是最小值和最大值。 
   然后，每次对中值M，查看矩阵中有多少个元素小于等于它（240的变种方法，关键是只花费n时间），
   最后，M缩减到一个值（是缩减到最小，不存在提前返回）时，矩阵中恰有k个元素<=它，那么就是答案。 
理解：满足kth（矩阵中恰有k个元素小与等于）的值有很多个，但是只要其中最小的，因为最小的必然等于矩阵中的一个值，刚好满足题目需要。 还有一种情况，[[1,2],[1,3]]，1的时候，最小值1也至少比两个数要大，此时返回1即可。

时间复杂度为O(n * logX)，X表示矩阵中的最大值减去最小值
'''

#  faster than 98.81% of Python3
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        start, end = matrix[0][0], matrix[-1][-1]
        
        '''
        这里算的方法，从左下向右上走。按列统计
        如果过大，就减小一行；
        如果小于等于，向右前进一步。
        当前的count：算的是当前位置前一列，当前行一直到最上都满足条件。
        比如现在在i，j，那么(0,j-1)(1,j-1)...(i,j-1)都满足，一共有i+1个
        然后这样遍历每一列，即j从0到len(matrix[0]),累加即最后的count
        '''
        def count_num(mid):
            count = 0
            i, j = m - 1, 0
            while i >= 0 and j < n:
                if matrix[i][j] > mid:
                    i = i - 1
                else:
                    j = j + 1
                    count += i + 1
            return count 
        
        '''
        这里如果是start<end，答案就好理解，因为跳出后start=end所以返回start
        但是当start<=end时，因为判断是count<k时，start进一，所以到最后start一定是第一个满足条件的，所以返回start
        '''
        while start <= end:
            mid = (start + end) // 2 
            count = count_num(mid)
            if count < k:
                start = mid + 1
            else:
                end = mid - 1
            
        return start
