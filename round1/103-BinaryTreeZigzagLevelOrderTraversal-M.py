'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''

# faster than 67.77% of Python3
def zigzagLevelOrder(root):
    result = []
    if not root:
        return result
    stack = []
    stack.append(root)
    flag = 0
    while stack:
        r = []
        temp = []
        for v in stack:
            r.append(v.val)
            if v.left:
                temp.append(v.left)
            if v.right:
                temp.append(v.right)
        if flag:
            r = r[::-1]
        result.append(r)
        flag = 1 - flag
            
        stack = temp
    return result