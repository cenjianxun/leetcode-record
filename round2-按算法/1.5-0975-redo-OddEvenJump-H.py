'''
975. Odd Even Jump

You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.
'''

'''
硬做
'''
def oddEvenJumps(self, arr: List[int]) -> int:
    n, res, = len(arr), 0
    # odd, even = [], []
    for i in range(n):
        jump = 1
        j = i  
        while 0 <= j < n:
            # print(i, j, jump)
            if j == n - 1:
                res += 1
                break
            if jump%2:
                # print(j, [(arr[k], k) for k in range(j + 1, n) if arr[k] >= arr[j]])
                _, j = min([(arr[k], k) for k in range(j + 1, n) if arr[k] >= arr[j]], default=(-1, -1))
            else:
                # print(j, [(arr[k], k) for k in range(j + 1, n) if arr[k] <= arr[j]])
                _, j = max([(arr[k], -k) for k in range(j + 1, n) if arr[k] <= arr[j]], default=(-1, 1))   
                j = -j
            jump += 1
            # print(i, j)
    return res

'''
1. 每一步的next都是固定的————则可以creat一个数组存起它们
2. 因为要求的是[大于/小于当前的]【最大/小的值】，所以先以.值.排.序。 如果说的是[大于/小于当前的]【最近值】，则按原序，即位置排序。
3. 然后需要使用dp解决：因为前一个的状态，需要后一个的状态决定，同时有初始状态，所以倒叙dp
这个如果依次循环，仍然需要二重循环。这时候可以看看是否存在 后一个需要前一个状态就可以决定 这种（或倒叙）。
'''
def oddEvenJumps(self, A: List[int]) -> int:
    def get_jump_location(B):
        ans = [-1] * len(A)
        stack = []  # 单调递减栈
        for i in B:
            while stack and i > stack[-1]:
                # 弹出栈顶比较小的索引stack_top，并且记录这些索引下一步全都会跳跃到索引 i
                stack_top = stack.pop()
                ans[stack_top] = i
            stack.append(i)
        return ans

    N = len(A)
    # B存储的是A中index的递增排序，排序规则为A[i]大小
    B = sorted(range(N), key=lambda i: A[i])

    # odd_next[i]存储位于索引 i 在奇数次跳跃时将会跳到的位置
    # 奇数跳跃时，前进的格子必须比当前要大，所以需要index按照对应A[i]的递增排序
    odd_next = get_jump_location(B)

    # 偶数跳跃时，前进的格子必须比当前要小，所以需要index按照对应A[i]的递减排序
    B.sort(key=lambda i: -A[i])
    even_next = get_jump_location(B)

    # odd[i]/ even[i] 为DP数组，代表从i进行奇数/偶数跳跃时能否到达末尾。
    odd = [False] * N
    even = [False] * N
    # 根据题意，数组末尾默认为好的起始索引
    odd[N - 1] = even[N - 1] = True

    for i in range(N - 2, -1, -1):
        # 注意一定要从数组倒数第二位开始倒着遍历，因为只有数组末尾的初始化状态是正确的，倒着遍历才能正确转移DP状态。
        if odd_next[i] != -1:
            # 先从odd_next拿到下一个能跳到的节点。接下来要进行偶数跳跃了，查询even，看看能不能跳到末尾。
            next_index = odd_next[i]
            odd[i] = even[next_index]
        if even_next[i] != -1:
            next_index = even_next[i]
            even[i] = odd[next_index]
    
    return sum(odd)