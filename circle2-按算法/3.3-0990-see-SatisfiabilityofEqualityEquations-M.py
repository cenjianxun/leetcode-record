'''
990. Satisfiability of Equality Equations

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
'''

'''
新算法
注意点：
p = find(parent[p]) 而不是find(p)
size初始化应该为1而不是0，否则size那边加不到
'''
def equationsPossible(self, equations: List[str]) -> bool:
    parent = list(range(26))
    size = [1] * 26
    
    def find(p):
        if parent[p] != p:
            p = find(parent[p])
        return p
    
    def union(p, q):
        pid, qid = find(p), find(q)
        if pid != qid:
            if size[pid] > size[qid]:
                parent[qid] = pid
                size[pid] += size[qid]
            else:
                parent[pid] = qid
                size[qid] += size[pid]
        '''
        if px != py:
            if rank[px] < rank[py]: 
                px, py = py, px    # rank balance
            p[py] = px
            rank[px] += rank[px] == rank[py]
        '''
                
    for x, e, _, y in equations:
        x, y = ord(x) - ord('a'), ord(y) - ord('a')
        if e == '=':
            union(x, y)
            
    for x, e, _, y in equations:
        x, y = ord(x) - ord('a'), ord(y) - ord('a')
        if e == '!':
            if find(x) == find(y):
                return False
    return True






    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x != parent_y:
                parent[parent_x] = parent_y            
            
        for x,sign,_,y in equations:
            x, y = ord(x) - ord('a'), ord(y) - ord('a')
            if sign == "=":
                union(x, y)
        
        for x,sign,_,y in equations:
            x, y = ord(x) - ord('a'), ord(y) - ord('a')
            if sign == "!":
                print(x, y, find(x), find(y))
                if find(x) == find(y):
                    return False
