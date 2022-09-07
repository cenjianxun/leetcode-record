'''
907. Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
'''

'''
单调用在：
如果是目前为止最小的，是一种情况；不是的话是另一种情况。
单调复用：
就是说 需要'前i个之和'->需要记录i值
单调栈情况：
可以存值也可以存index
需要栈而不是str的原因是：
要找到目前为止最小的，而这个值在第几个不确定
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp, stack, res = [0] * (n+1), [0], 0
        arr = [float('-inf')] + arr
        for i in range(1, n + 1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            # print(stack[0], arr[i])
            dp[i] = dp[stack[-1]] + (i - stack[-1]) * arr[i]
            # print(i, stack, dp)
            res += dp[i]
            stack.append(i)
        return res % (10**9 + 7)