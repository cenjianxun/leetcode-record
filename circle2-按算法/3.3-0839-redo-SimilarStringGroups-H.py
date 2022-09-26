'''
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
'''

'''
union find 继续：
套路：如果两两比较就必须双循环 O(n**2)
注意：
1. 如果要算几个圈，就必须单独新设置变量统计，每次union就-1
parents不能提供此功能，因为它记录的是树的整个路径，而不是单有root
2. 如果只要求count，可以不用平衡size
3. 函数内的函数不能共用str，但可以共用list
（上道题里的[]可以直接用，这里的count不行，必须self） ### 待解决
'''
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.count = n = len(strs)
        # size = [1] * len(strs)
        
        groups = list(range(len(strs)))
        def find(p):
            if groups[p] != p:
                p = find(groups[p])
            return p
            
        def union(p, q):
            pid, qid = find(p), find(q)
            
            if pid != qid:
                # if size[pid] >= size[qid]:
                #     groups[qid] = pid
                #     size[pid] += size[qid]
                # else:
                #     groups[pid] = qid
                #     size[qid] += size[pid]    
                groups[qid] = pid
                self.count = self.count - 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    # print(i,strs[i], j, strs[j])
                    union(i, j)
        print(groups)
        return self.count          
            
            
    def isSimilar(self, p, q):
        if len(p) != len(q):
            return False
        i = 0
        count = []
        while i < len(p):
            if p[i] != q[i]:
                count.append(i)
            i = i + 1
        if not count:
            return True
        if len(count) != 2:
            return False
        p = list(p)
        i , j = count
        p[i], p[j] = p[j], p[i]
        if ''.join(p) != q:
            return False
        return True   