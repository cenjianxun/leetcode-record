'''
979. Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
'''

def distributeCoins(self, root: Optional[TreeNode]) -> int:
    self.res = 0
    def dfs(left, right, val):
        if not left and not right:
            return val
        rest_l = rest_r = 0
        if left:
            left.val =  dfs(left.left, left.right, left.val)
            rest_l = left.val - 1
            self.res = self.res + abs(rest_l)
            val = val + rest_l
        if right:
            right.val = dfs(right.left, right.right, right.val)
            rest_r = right.val - 1
            self.res = self.res + abs(rest_r)
            val = val + rest_r
        return val
    if not root:
        return
    dfs(root.left, root.right, root.val)
    return self.res

'''
提升化简
'''
# faster than 55.38% of Python3
def distributeCoins(self, root: Optional[TreeNode]) -> int:
    self.res = 0
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        self.res = self.res + abs(left) + abs(right)
        return node.val + left + right - 1
 
    dfs(root)
    return self.res