'''
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

'''
超时
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        l = r = 0
        res = []
        print(len(s))
        while l < len(s):
            print(l,r,count)
            while l < len(s) and s[l] not in count:
                l = r = l + 1
            while r < len(s) and r < l + len(p):
                if s[r] not in count:
                    break
                count[s[r]] -= 1
                if count[s[r]] < 0:
                    break
                r += 1
                #print(r, s[r],count[s[r]])
            #print(l,r,count)
            if r == l + len(p):
                res.append(l)
                while r < len(s) and s[l] == s[r]:
                    l,r = l+1, r+1
                    res.append(l)
            count = Counter(p)
            l = r = l+1
        return res



'''
加快速度的地方：遍历找位置改为统计个数，加减个数
* Counter没有.remove, 用del 
'''
def findAnagrams(self, s: str, p: str) -> List[int]:
    from collections import Counter
    ls, lp = len(s), len(p)
    res = []
    count_p = Counter(p)
    count_s = Counter(s[:lp])
    i = len(p)
    while i <= ls:
        # print(i, count_s)
        if count_p == count_s:
            res.append(i - lp)
        if i < ls:
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_s[s[i - lp]] = count_s[s[i - lp]] - 1
            if not count_s[s[i - lp]]:
                del count_s[s[i - lp]]
            # print(i, s[i], count_s, res)
        i = i + 1
    return res

'''
定长窗口，每次只能比较最边边的那个，不能一开始拉伸后面定长挪，但是如果每次都创建新map来拉伸算就会超时
'''
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        cuts = Counter(s[:lp-1])
        countp = Counter(p)
        res = []
        for start in range(ls-lp+1):
            end = start + lp - 1
            cuts[s[end]] = cuts.get(s[end], 0) + 1
            if cuts == countp:
                res.append(start)
            cuts[s[start]] -= 1
            if not cuts[s[start]]:
                del cuts[s[start]]
        return res

'''
注意循环和+1的顺序
要先看0是否在，然后right要是后一个，循环里right最后加，因为while的条件是right < len
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLen, pLen = len(s), len(p)
        res = []
        if pLen > sLen:
            return res
        sCount, pCount = [0] * 26, [0] * 26
        for i in range(pLen):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1
        left, right = 0, pLen 
        '''
        print(pCount)
        if pCount == sCount:
            res.append(left)
        while right < sLen:
            sCount[ord(s[right]) - ord('a')] += 1
            sCount[ord(s[left]) - ord('a')] -= 1
            left += 1
            if pCount[ord(s[left]) - ord('a')]:
                if pCount == sCount:
                    res.append(left)    
            right += 1

        # 所以可以改成下面这个：
        '''
        if pCount == sCount:
            res.append(0)
        for i in range(sLen - pLen):
            sCount[ord(s[i]) - ord('a')] -= 1
            sCount[ord(s[i + pLen]) - ord('a')] += 1
 
            if pCount == sCount:
                res.append(i+1)      
        return res

'''
diff也可以不预先统计，将它转变为遍历s的时候一种“消耗品”——当“消耗品”不足，唯一可以做的就是移动左窗口释放一些出来
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        sLen, pLen = len(s), len(p)
        res = []
        pCount = Counter(p)      
        lo = hi = 0
        while hi < sLen:
            #print(lo, s[lo], hi, s[hi], pCount)
            if pCount[s[hi]] > 0:
                pCount[s[hi]] -= 1
                hi += 1
                if hi - lo == pLen:
                    res.append(lo)
            else:
                pCount[s[lo]] += 1 
                lo += 1
        return res