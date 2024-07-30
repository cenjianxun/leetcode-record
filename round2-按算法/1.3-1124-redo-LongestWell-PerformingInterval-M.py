'''
1124. Longest Well-Performing Interval

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.
'''

'''
1. 把无意义的数值去掉，只用有限有意义的值代替，叫 归一化
2. 求什么：求和为正的最长子序列 -> 需要知道前缀和
3. 前缀和可以知道任意区间的值之和 nums[i]+nums[i+1]+...+nums[j] = sums[j] - sums[i]
(差分：diff[i]就是nums[i]-nums[i-1]，用于给每个i-j区间增加/减少值)
4. 分别优化左端点i和右端点i
5. 左端点的集合是单调递减，因为在j右边且值比sums[j]还大的肯定不是最优解，没有j优，所以比j右的，值需要比sums[j]小，它有几率遇到不能匹配j的值，which可能是最终解。
单调栈的启用，是，就是刚好所需要的值（其中一个边界值），是极值的集合。
6. 因为求的是最远的，而不是邻居的那个，所以需要先全部入栈一次。（or 入栈一个就倒着遍历）
7. 右端点的遍历，从后至前，是因为贪心，需要最远。
8. 右端点算的过程中，stack内可以pop，因为，右端点倒序逼近，这一轮的j如果减同一个i，一定比上一轮结果小，所以可以舍弃这个i
'''
def longestWPI(self, hours: List[int]) -> int:
    n, res = len(hours), 0
    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        t = 1 if hours[i-1] - 8 > 0 else -1
        sums[i] = sums[i-1] + t
    stack = []
    print(sums)
    for i in range(n, -1, -1):
        for j in range(i):
            # print(i, j, sums[i] - sums[j])
            if sums[i] - sums[j] > 0:
                print(i, j, sums[i], sums[j])
                res = max(res, i - j)
                break
    return  res
'''
我来分析一下思路
首先做一下归一化，满足要求的工作时间记录为1，不满足的记录为-1，那么这道题本质就是求和为正的最长连续子序列

由于需要求子序列的和，所以一般将数组转为前缀和数组，即新数组的第i个元素，是原数组前i个元素的和。这样求一个[i,j]子序列的长度只需要aj-ai就可以了

我们先用枚举的思路考虑一下。以第i个元素结尾的最长正和子序列是什么呢？容易想到是所有比i小的j中，满足aj < ai的最小的j。
所以最简单的做法就是遍历每个元素，尝试找出那个j就可以了，复杂度是o(n^2)

接下来我们看一下优化手段：

1. 寻找j的过程是否需要从0遍历到i呢？
当我们发现ai <= a0时，其实可以把所有x排除掉（ax>=a0），因为ax >= a0 >= ai，必然无法形成正和子序列。去除这些元素后的数组再判断a0和ai的大小关系，不断迭代。
那么每一迭代用到的a0是什么数呢？容易发现是一个以a0为起始的单调递减的序列。这个序列我们能够通过o(n)的遍历提前寻找到。
所以我们可以将j的寻找次数从i次优化为单调递减序列的长度

2. 每个i是否都必须遍历整个单调序列呢？
case1：i无法构成以它结尾的正和子序列
只需看单调序列中的末尾元素即可，如果末尾元素不可以，其他元素都不行，因为单调序列的其他元素都比末尾元素大
case2：i能够构成以它结尾的正和子序列
假定i1找到了j1是其最长的正和子序列
若i2<i1，且能够找到比i1更优的最长正和子序列j2，一定有j2 < j1，因为i1-j1 < i2 -j2，故j1-j2 > i1-i2>0

那么我们的算法就有了：
1. 构建前缀和数组A
2. 构建单调递减的栈B
3. 倒序遍历A，下标为i：
    3.1 若B.top >= i，则B.pop，直到B为空退出或B.top<i
    3.2 若A[B.top] < A[i]，则更新序列长最大值，B.pop，直到B为空退出或者A[B.top] >= A[i]（这步是寻找以i结尾的最长正和序列。由case2证明可知，B出栈的元素未来是不可能最为最长正和序列的端点）
    3.3 迭代（由case1可知，只要栈尾元素不符合要求，i就不能构成新的正和子序列）
'''

'''
stack的作用是贪心达到最远
'''
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        L = len(hours)
        preSum = [0]
        for i in range(L):
            preSum.append(preSum[-1] + (1 if hours[i] > 8 else -1))
        res = 0
        #print(preSum)
        # for i in range(L):
        #     for j in range(i+1, L+1):
        #         if preSum[j] > preSum[i]:
        #             res = max(res, j - i)
        stack = []
        for i in range(L+1):
            if not stack or preSum[stack[-1]] > preSum[i]:
                stack.append(i)
        for i in range(L, -1, -1):
            while stack and preSum[stack[-1]] < preSum[i]:
                res = max(res, i - stack.pop())
        return res