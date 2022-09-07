''' 
968. Binary Tree Cameras

You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.
'''

'''
状态机：
三种状态：
0：放了cam
1：没放cam，但被cover
2：没放cam，且没被cover
'''
def minCameraCover(self, root: Optional[TreeNode]) -> int:
    '''
    三种状态：
    0：放了cam
    1：没放cam，但被cover
    2：没放cam，且没被cover
    '''
    def dfs(node):
        if not node:
            return float('inf'), 0, 0
        l0, l1, l2 = dfs(node.left)
        r0, r1, r2 = dfs(node.right)
        t0 = min(l0, l1, l2) + min(r0, r1, r2) + 1
        t1 = min(l0 + min(r0, r1), r0 + min(l0, l1))
        t2 = l1 + r1
        return t0, t1, t2
    t0, t1, t2 = dfs(root)
    return min(t1, t0)