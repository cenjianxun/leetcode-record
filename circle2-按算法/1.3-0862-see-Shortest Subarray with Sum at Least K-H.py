'''
862. Shortest Subarray with Sum at Least K
Hard

n integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:

    Input: nums = [1], k = 1
    Output: 1

Example 2:

    Input: nums = [1,2], k = 4
    Output: -1

Example 3:

    Input: nums = [2,-1,2], k = 3
    Output: 3
 

Constraints:

    1 <= nums.length <= 105
    -105 <= nums[i] <= 105
    1 <= k <= 109
'''

'''
数学。 积分。 要保持积分递增

用数组 P 表示数组 A 的前缀和，即 P[i] = A[0] + A[1] + ... + A[i - 1]。我们需要找到 x 和 y，使得 P[y] - P[x] >= K 且 y - x 最小。

我们用 opt(y) 表示对于固定的 y，最大的满足 P[x] <= P[y] - K 的 x，这样所有 y - opt(y) 中的最小值即为答案。我们可以发现两条性质：

1 如果 x1 < x2 且 P[x2] <= P[x1]，那么 opt(y) 的值不可能为 x1，这是因为 x2 比 x1 大，并且如果 x1 满足了 P[x1] <= P[y] - K，那么 P[x2] <= P[x1] <= P[y] - K，即 x2 同样满足 P[x2] <= P[y] - K。

2 如果 opt(y1) 的值为 x，那么我们以后就不用再考虑 x 了。这是因为如果有 y2 > y1 且 opt(y2) 的值也为 x，但此时 y2 - x 显然大于 y1 - x，不会作为所有 y - opt(y) 中的最小值。
 
'''
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0] 
        for i in range(len(nums)):
            if nums[i] >= k:
                return 1
            preSum.append(preSum[-1] + nums[i])
        queue = deque()
        res = float('inf')
        for i, n in enumerate(preSum):
            while queue and queue[-1][1] >= n:
                queue.pop()
            while queue and n - queue[0][1] >= k:
                res = min(res, i - queue[0][0])
                queue.popleft()
            queue.append((i, n))
        return -1 if res == float('inf') else res