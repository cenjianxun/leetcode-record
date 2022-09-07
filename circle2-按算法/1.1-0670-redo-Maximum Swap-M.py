'''
670. Maximum Swap
Medium

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

	Input: num = 2736
	Output: 7236
	Explanation: Swap the number 2 and the number 7.

Example 2:

	Input: num = 9973
	Output: 9973
	Explanation: No swap.
 
Constraints:

	0 <= num <= 108
'''

'''
要考虑的实在太多了：
9973：为空时
98368：要换的首位不是整个的首位时
1993/10909091 ：最大那个值应该是最后一个最大值

“第一个小值和尽可能最后的最大值交换”：
第一个小值：要记录每个值的位置
'''

#faster than 26.28% of Python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        i = 0
        maxi = num.index(max(num))
        while maxi == i and i < len(num)-1:
            i += 1
            maxi = num.index(max(num[i:]), i)
        print(i, maxi)
        for j in range(len(num)-1, maxi-1, -1):
            if num[j] == num[maxi]:
                maxi = j
                break
        num[i], num[maxi] = num[maxi], num[i]
        return ''.join(num)

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxnum = sorted(num, reverse=True)
        left = 0
        for i in range(len(num)):
            if num[i] != maxnum[i]:
                left = i
                break
        right = left
        print(num, maxnum, left)
        for i in range(len(num)-1, left, -1):
            if num[i] > num[right]:
                right = i
        num[left], num[right] = num[right], num[left]
        return ''.join(num)

'''
所以考虑所有情况，包括重复，应该是：
对被交换的最小值，应该尽量选最前面的。这里最小值的意思是，比要交换的最大值小的就行
对被交换的最大值，应该选最后一个，而且应该在这个最小值的后面。
所以步骤是：
1.先找降序的最低点
2.在找最低点之后的最大值
❣3.再从最后倒着找等于最大值的index
4.再从最低点倒着找比最大值小的最早的index
'''