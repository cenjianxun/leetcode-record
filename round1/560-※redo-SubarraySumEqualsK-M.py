'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

'''
精髓在于dp[i，j] = dp[0，j] - dp[0，i-1]
所以一行就可以搞定
记录所有的dp[0，i-1]及个数，即从头到i-1为止的和及个数。
那么当前和dp[0，j] - k的值如果存在，就表明有一个i-j段（i未知）满足条件

* 要约定dic[0] = 1先，因为当满足条件的是0-j段的时候，
即dp[0][j]就等于k，dp[0][i-1]是第0个数之前，也需要占位
map.put(0, 1)，如果遇到第一个index有map.get(sum - k == 0), 说明从0到index的sum == k


'''
# faster than 87.30% of Python3
def subarraySum(self, nums: List[int], k: int) -> int:
    l = len(nums)
    dic = {0:1}
    sums = 0
    res = 0
    for n in nums:
        sums = sums + n
        if sums - k in dic:
            res = res + dic[sums - k]
        dic[sums] = dic.get(sums, 0) + 1
        # print(n, sums, dic, res)
    return res


'''
211101
上面这个 巧妙的方式是不用看dic里面再判断是不是j>i;
而是边算边加入，那么自然限制了边界
边算边加入适用于，可以自然需要部分（限制的）。先入全部适用于，需要全局的。
'''

def subarraySum(self, nums: List[int], k: int) -> int:
    n, res = len(nums), 0
    sums, count  = [0] * (n + 1), defaultdict(set) 
    for i in range(n + 1):
        if i > 0:
            sums[i] = sums[i - 1] + nums[i-1]
        count[sums[i]].add(i)
    print(sums)
    for i in range(n + 1):
        rest = k + sums[i]
        if rest in count:
            for j in count[rest]:
                if j > i:
                    res += 1
    return res

'''
什么奇淫技巧
sums[i] 为0-i的和，则sums[j]-sums[i]为i-j之和
任意一个(i,j)之和为k，相当于sums[j]-sums[i] = k，相当于sums[j]-k = sums[i]，而j比i大，到j时，所有sums[i]都在dic里。
反正就是prefix sum，跟path sum III一个套路，用map存prefix sum的frequency
'''