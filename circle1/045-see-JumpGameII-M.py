'''
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

'''
还是最远范围的问题
注意的点是max范围的取值
'''
# faster than 94.58% of Python3
def jump(self, nums: List[int]) -> int:
    # dp = [0] * len(nums)
    i, j = 0, 1
    step = 0
    while j < len(nums):
        fur = max([(k + nums[k], k) for k in range(i, j)])
        step = step + 1
        i, j = fur[1],  fur[0] + 1
    return step


# 改进：
def jump(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    rightmosts = [i + nums[i] for i in range(len(nums))]
    start, end = 0, 0
    step = 0        

    while end < len(nums) - 1:
        start, end = end, max(rightmosts[start: end + 1])
        if end == start:
            return -1
        step += 1
    
    return step
'''
贪心: 我们每次贪心的找在自己当前能到达的几个位置里面，跳到哪个位置的时候，在下一步能跳的最远。然后，我们当前步就跳到这个位置上去，所以我们在这一步的跳跃时，给下一步留下了最好的结果。

贪心要有两个变量 一个是最远的范围，一个是当前的位置
'''
def jump(self, nums: List[int]) -> int:
    reach, cur, steps = 0, 0, 0
    for i in range(len(nums) - 1):
        reach = max(reach, i + nums[i])
        if i == cur:
            cur = reach
            steps = steps + 1
    return steps