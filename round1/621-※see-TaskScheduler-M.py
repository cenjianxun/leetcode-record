'''
621. Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''

'''
思路：
分界是字母的个数和必须跳过的个数n
必须跳过的个数n，相当于二维矩阵的宽
如果字母个数小于n，相当于这个矩阵可以装下它，否则就要挑选合适字母的装它
len()<n（可以装下）时，直接求矩阵面积，矩阵高是最长的字母的个数，最后再减去最后一行的空
len()>n（需要pick）时，挑选的标准是，尽量不要产生比当前最小个数更小的个数：保持尽量平均

point：
1. n是不能挨着的值，那么一轮字母个数是n+1
2. 那么二维矩阵最大宽度是n+1
3. 注意倒数第二-倒数第一的差值比倒数第一的值还大的时候
4. 注意倒数第二的取法
5. 注意当所有字母个数相等的时候，仍然是keep尽量平均的思想，所以gap = 1


'''
# faster than 40.87% of Python3
def leastInterval(self, tasks: List[str], n: int) -> int:
    from collections import Counter
    if not n:
        return len(tasks)
    dic = Counter(tasks)       
    count  = list(dic.keys())
    # n = n + 1
    print(dic)
    num = 0
    while count:
        # count.sort(key = lambda x:dic[x], reverse = True)
        count.sort(key = lambda x:(dic[x], x), reverse =  True)
        while not dic[count[-1]]:
            count.pop()
        if len(count) <= n + 1:
            i = 1
            while i < len(count) and dic[count[0]] == dic[count[i]]:
                i = i + 1
            # print(count[0], dic[count[0]], n, i )
            num = num + dic[count[0]] * (n+1) - (n + 1 - i)
            break
        else:
            i = n
            while i >= 0 and dic[count[i]] == dic[count[-1]]:
                i = i - 1
            gap = 1 if i < 0 else min(dic[count[-1]], dic[count[i]] - dic[count[-1]])

            num = num + gap * (n + 1)
            for i in range(0, n + 1):
                dic[count[i]] = dic[count[i]] - gap 

    return num


'''
我服了。蠢。填空。任务占时+空闲时间

当最多的任务的个数（列数）填不满除了它以外的任务个数时，答案都是len(tasks)
like: ["A","A","B","C","D","E","F"] 1
如果列数超过了 n+1，那么就算没有这些待命状态，任意两个相邻任务的执行间隔肯定也会至少为 n。此时，总执行时间就是任务的总数 ∣task∣ 
'''
# faster than 93.06% of Python3
def leastInterval(self, tasks: List[str], n: int) -> int:
    from collections import Counter
    if not n:
        return len(tasks)
    dic = Counter(tasks)       
    max_count = max(dic.values()) 
    rest = 0
    for k, v in dic.items():
        if v == max_count:
            rest = rest + 1
    return max(len(tasks), (max_count - 1) * (n+1) + rest)