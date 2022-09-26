'''
721. Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
'''


# faster than 5.01% of Python3
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        people, size = list(range(n)), [1] * n
        
        def find(p):
            if p != people[p]:
                p = find(people[p])
            return p
        
        def union(p, q):
            pid, qid = find(p), find(q)
            if pid != qid:
                if size[pid] < size[qid]:
                    pid, qid = qid, pid
                people[qid] = pid
                size[pid] += size[qid]
 
        for i in range(n - 1):
            for j in range(n):
                if self.isOnePerson(accounts[i], accounts[j]):
                    union(i, j)
                    
        dic = {}
        res = []
        for i in range(n):
            iid = find(i)
            if iid not in dic:
                dic[iid] = set()
            dic[iid] = dic[iid] | set(accounts[i][1:])
  
        for k in dic:
            acc = [accounts[k][0]] + sorted(list(dic[k]))
            # print(acc)
            res.append(acc)
        return res
    
    
    def isOnePerson(self, p, q):
        if set(p[1:]) & set(q[1:]):
            return True
        return False


'''
好标致好快
循环account的方式不一样，可以变很快：
第一层把name摘出来，第二层循环email，
dic的设置是key=具体内容，value = 根id
这样union的两个对象是当前序号id和dic[email](也是id)

提高速度的：
1.list切片
2.把UF单独弄出去了（不懂）
'''
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()


'''
如果parent是列表，值就一定是index
如果parent是map，值可以是string，总之parent的索引和值的类型一定要相同就行。

union里的内容是，条件里要求它俩有联系，或是希望它俩有联系的俩值。
如果是list，就联系之前有关联的index和当前的index
如果是map，就联系类型相同的东西，本题是联系同个人的email，被关联的选随便一个email就行，email[0]就行

'''