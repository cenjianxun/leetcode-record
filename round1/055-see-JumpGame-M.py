'''
55. Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''

'''
不会做 无语
'''

def canJump(nums: List[int]) -> bool:
    step = 0
    for i in range(len(nums)):
        if step < i:
            return False
        step = max(step, i + nums[i])
        if step >= len(nums) -1:
            return True

'''
会了
 ↑ ↑ 原来可以用i>step
'''
def canJump(nums: List[int]) -> bool:
    fur = nums[0]
    i = 0
    while i <= fur:
        if fur >= len(nums) - 1:
            return True
        if nums[i] + i > fur:
            fur = nums[i] + i
        i = i + 1
    if fur >= len(nums) - 1:
        return True
    else:
        return False  


'''
220602
深度？ 超时
'''
def canJump(self, nums: List[int]) -> bool:
    farreach = [nums[i] + i for i in range(len(nums))]
    #print(farreach)
    def canReach(nums, n):
        print(n)
        if n == 0:
            return True
        for i in range(n - 1, -1, -1):
            if nums[i] >= n and canReach(nums, i):
                return True
        return False

    return canReach(farreach, len(nums) - 1)

'''
用dp 好厉害我
'''
def canJump(self, nums: List[int]) -> bool:
    dp = [False] * len(nums)
    dp[-1] = True
    nearest = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i >= nearest:
            dp[i] = True
            nearest = i
    return dp[0]