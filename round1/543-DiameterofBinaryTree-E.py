'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

# faster than 13.14% of Python3
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        return self.helper(root, 0, 0)
    
    def helper(self, root, lens, res):
        if not root:
            return res
        left = self.getDepth(root.left, 0)
        right = self.getDepth(root.right, 0)
        # print(root.val, left, right, res)
        res = max(res, left + right)
        if lens > left + right:
            return res
        else:
            if left > right:
                return self.helper(root.left, left, res)
            else:
                return self.helper(root.right, right, res)
        
        
    def getDepth(self, root, step):
        if not root:
            return step
        left = self.getDepth(root.left, step + 1)
        right = self.getDepth(root.right, step + 1)
        return max(left, right)


'''
题里的直径长是连接点的边的个数（比点的个数少一）
'''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root ):
   
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right)
            #print(root.val, left, right, self.res)
            return 1 + max(left, right)
        dfs(root)
        return self.res