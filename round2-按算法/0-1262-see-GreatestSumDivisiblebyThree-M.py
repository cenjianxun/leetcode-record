'''
1262. Greatest Sum Divisible by Three

Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
'''

'''
剩余的比较是 先横再纵 vs 先纵再横，两者都要两个都有
'''
# faster than 76.33% of Python3
def maxSumDivThree(self, nums: List[int]) -> int:
    res = 0
    rest1 = []
    rest2 = []
    nums.sort()
    for n in nums:
        if not n%3:
            res = res + n
        if n%3 == 1:
            rest1.append(n)
        if n%3 == 2:
            rest2.append(n)
    if len(rest1) < len(rest2):
        rest1, rest2 = rest2, rest1
    
    l1, l2 = len(rest1), len(rest2)
    # print(rest1, rest2, l1, l2)
    while l2 > 2:
        res = res + rest1.pop() + rest2.pop()
        l1, l2 = l1 - 1, l2 - 1
    print(res, rest1, rest2)
    sum1 = 0
    while l2 > 0:
        sum1 = sum1 + rest1[l1-1] + rest2[l2-1]
        l1, l2 = l1 - 1, l2 - 1
    sum1 = sum1 + sum(rest1[l1%3:l1])
    sum2 = sum(rest1[len(rest1)%3:])
    rest1 = rest1[:len(rest1)%3]
    # print(rest1)
    while rest1 and rest2:
        sum2 = sum2 + rest1.pop() + rest2.pop()
    return res + max(sum1, sum2)

'''
改进：从总和记录多余的，做减法。记录余1的最小和次小，余2的最小和次小
'''

'''
dp: 状态机：
有三个状态
→ 新进一个数时三个状态互相转换
最终求的值是最后的某一个状态
'''
def maxSumDivThree(self, nums: List[int]) -> int:
    state = [0, float('-inf'), float('-inf')]

    for num in nums:
        if num % 3 == 0:
            state = [state[0] + num, state[1] + num, state[2] + num]
        if num % 3 == 1:
            a = max(state[2] + num, state[0])
            b = max(state[0] + num, state[1])
            c = max(state[1] + num, state[2])
            state = [a, b, c]
        if num % 3 == 2:
            a = max(state[1] + num, state[0])
            b = max(state[2] + num, state[1])
            c = max(state[0] + num, state[2])
            state = [a, b, c]
    return state[0]