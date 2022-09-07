'''
239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''

''' redo
精髓在于，如果win里面只要有任何数字小于要进来的那个，就把她们通通删掉。 精妙的是这样会导致win[0]永远是最大的那个。
还要注意的是，左边删右边进以及权衡的顺序，是先删，再有门槛的筛选，再放进
以及，当前的永远放进。这个没有关系，且必要。因为每个值都需要审。
'''
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    win = []
    for i, n in enumerate(nums):
        if i >= k and win[0] <= i - k:
            win.pop(0)
        while win and nums[win[-1]] <= n:
            win.pop()
        win.append(i)
        if i >= k - 1:
            res.append(nums[win[0]])
        # print(win, res)
    return res

'''
211021
单调队列，是把'只要比当前小/大的值都放进去'
这个方法解决 如果当前最大值被淘汰了，找不到次大值的问题
找最大值，在栈里的就是递减队列，第一个就最大。

本题额外注意的点：
1. 在k值及以上需要判断首值是否需要pop
2. 在k-1时，就需要append进res
3. 先popleft再append

另外一种思想是重新定义push和pop，
在新定义的函数内部进行判断和动作
'''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        pre_max = []
        for i, n in enumerate(nums):
            while pre_max and nums[pre_max[-1]] < n:
                pre_max.pop()
            pre_max.append(i)
            if pre_max[0] <= i-k:
                pre_max.pop(0)

            if i >= k - 1:
                res.append(nums[pre_max[0]])
            #print(i, n,pre_max, res)
        return res