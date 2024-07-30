'''
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts
'''
# faster than 100.00% of Python3
def partitionLabels(self, s: str) -> List[int]:
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = []
        dic[s[i]].append(i)
    # print(dic)
    stack = [[v[0],v[-1]] for k, v in dic.items()]
    stack.sort()
    # print(stack)
    res = []
    temp = stack[0]
    for s in stack:
        if s[0] <= temp[1]:
            if s[1] > temp[1]:
                temp[1] = s[1]
        else:
            res.append(temp )
            temp = s
    res.append(temp )
    # print(res)
    res = [r[1]-r[0]+1 for r in res]
    return res

'''
只记录末尾就行
'''

# faster than 70.82% of Python3
def partitionLabels(self, s: str) -> List[int]:
    dic = {c:i for i, c in enumerate(s)}
    # print(dic)
    res = []
    pre = i = j = 0
    for i, c in enumerate(s):
        j = max(j, dic[c])
        if i == j:
            res.append(i - pre + 1)
            pre = i + 1
    return res