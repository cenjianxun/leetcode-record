'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''

'''
思想就是，用dic记住还有几个没进，进一个减一个，如果空了就记一个res，
进stack，右扩左缩，什么时候缩呢，就是stack里最左边的数的个数，多于它本应有的个数，左边就缩。
卡在的点是，如果dic空了，进行下一轮时，是stack左边强行缩一个，这时dic里面是只有这一个，而不是只缺这一个。
'''
# faster than 5.05% of Python3
# less than 9.43% of Python3
from collections import Counter, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        stack = deque()
        res = s
        tdic = Counter(t)
        flag = 0
        for i in range(len(s)):
            # print(i, s[i], stack, tdic, res)
            if s[i] in t:
                stack.append(i)
                if tdic[s[i]] > 0:
                    tdic[s[i]] = tdic[s[i]] - 1
                while stack:
                    index = stack[0]
                    cur = s[stack[0]:stack[-1]+1]
                    # print(stack, tdic, cur)
                    if cur.count(s[index]) + tdic.get(s[index], 0) >  t.count(s[index]):
                        stack.popleft()
                    else:
                        break
                if s[i] in tdic and not tdic[s[i]]:
                    tdic.pop(s[i])

            # print(i, s[i], stack, tdic, res)
            if not tdic and stack:
                flag = 1
                cur = s[stack[0]:stack[-1]+1]
                res = cur if len(res) > len(cur) else res
                index = stack.popleft()
                tdic[s[index]] = 1

                # print(cur, res)
                        
        return res if flag else ''


'''
改了别人的c代码
之前没想通的地方：
为什么长度可以作为判定依据？如果长度相同内容不同呢？
结果是：长度还是依据dic，做计数dic的下一级。只有dic>=0, 意思是相对应的字母算到了，长度才+1

and 修改的小地方：min_len > i -left +1 改成>=
因为把初始min_len 设成len(s)了
'''
# faster than 70.96% of Python3
# less than 66.51% of Python3
def minWindow(self, s: str, t: str) -> str:
    left, cnt, min_len = 0, 0, len(s) 
    dic_t = Counter(t)
    res = ''

    for i in range(len(s)): 
        if s[i] in dic_t:
            dic_t[s[i]] = dic_t[s[i]] - 1
            if dic_t[s[i]] >=0:
                cnt = cnt + 1
        # print(s[i], cnt, dic_t)
        while cnt == len(t):
            if min_len >= i - left + 1:
                min_len = i - left + 1
                res = s[left:left + min_len]
            # print(left,s[left], i, s[i], dic_t, res)
            if s[left] in dic_t:
                dic_t[s[left]] = dic_t[s[left]] + 1
                if dic_t[s[left]] > 0:
                    cnt = cnt - 1
            left = left + 1
    return res

'''
初始结构：
需要记录需要字符及个数的字典
还需要记录现存的，字典，or这里可以简化为num

仍然需要注意的是，
如果长度相等，需要循环，而不是一遍过。
因为可能出现需要的某些元素重复出现，多余的情况。
多余的时候，字典里的记录就会<0，什么时候合格呢，>0的时候。

所以窗口挪动的时候，一定要在循环里把所有情况都解决了才行，因为右边窗口是匀速前进的
'''
def minWindow(self, s: str, t: str) -> str:
    tdic, cnt = Counter(t), 0
    l = r = start = end = 0
    while r < len(s):
        # print(cnt, l, s[l], r, s[r])
        if s[r] in tdic:
            tdic[s[r]] -= 1
            if tdic[s[r]] >= 0:
                cnt += 1
        while cnt == len(t):
            if s[l] in tdic:
                if not end or end - start >  r + 1 - l:
                    start, end = l, r + 1
                tdic[s[l]] += 1
                if tdic[s[l]] > 0:
                    cnt -= 1
            l += 1
        r += 1

    return s[start:end]

'''
这个方法太牛了

1. missing减至0就不再动，意思是除了开始，从此以后handle的范围里都不会缺
这样满了之后，每一轮都试一次而已
2. 如果不在要求里，意思是初始就为0，每轮必减当前的c，没有的就减为负数
如果在要求的里，第二个进来之后，也减为负。那么进入while循环，如果为负，又加上来，
但是不留恋，那么跳出循环的必是下一个为0的，即一定是在要求里的字符。
而且如果存在在范围里的，有多余的t，那么它加1还是为负，所以还是会继续轮下去，直到碰到第一个满足条件个数的t中元素
'''
    def minWindow(self, s: str, t: str) -> str:
        winCount = Counter(t)
        winLen = len(t)
        i, start, end = 0, 0, 0

        for j, e in enumerate(s, 1):
            
            if winCount[e] > 0:
                winLen -= 1
            winCount[e] -= 1
            # print(j, e, winLen, winCount)
            if winLen == 0:  
                while winCount[s[i]] < 0:
                    winCount[s[i]] += 1
                    i += 1
                    
                #print(j,i,end,start)
                if end == 0 or j - i < end - start:
                    start, end = i, j
        return s[start:end]   

'''
总体思路：
1. 要先选定用什么方式来确定一个窗口包含T？
    一个map 算count + 一个int算len
2. 怎么判断最小？
    到了达到1的标准记录并比较


点：
1.while里面必须map先+1，i后+1
2.end（J）必须初始=0，并单独讨论end没移动的情况（not J）, 不能设end = len，这样当没一个匹配的时候，会默认为default
3.在当第一次匹配所有的时候，winLen就不需要（计数）了，因为后续窗口不会因为不够而扩张，只会因为瞄准到下一个而平移了。

'''

'''
测试用例：！！ "a" "aa" || "a" "b"
如果end没设特殊符合就要在条件里单独考虑。否则要在return时加
return [start:end] if end xxx  else ''

'''

    def minWindow(self, string: str, pattern: str) -> str:
        from collections import defaultdict
        if not string or not pattern:
            return ''
        p_count = Counter(pattern)
        p_len = len(pattern)
        i = j = 0
        start, end = 0, -1

        while j < len(string):

            if p_count[string[j]] > 0:
                p_len -= 1
            p_count[string[j]] -= 1
            if p_len == 0:
                while p_count[string[i]] < 0:
                    p_count[string[i]] += 1
                    i += 1
                if end == -1 or end - start > j - i:
                    start, end = i, j
                p_count[string[i]] += 1
                i += 1  
                p_len += 1      
            j += 1
        return string[start:end + 1]