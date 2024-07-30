'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

'''
用太久 faster than 6.18% of Python3
'''
def levelOrder(root): 
    result = []
    if not root:
        return result
    stack = []
    stack.append(root)
    while stack:
        r = []
        temp = []
        for v in stack:
            r.append(v.val)
            if v.left:
                temp.append(v.left)
            if v.right:
                temp.append(v.right)
        result.append(r)
        stack = temp
    return result

'''
加速
'''
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        res.append([s.val for s in stack])
        temp = []
        for r in stack:
            r.left and temp.append(r.left)
            r.right and temp.append(r.right)
        stack = temp
    return res