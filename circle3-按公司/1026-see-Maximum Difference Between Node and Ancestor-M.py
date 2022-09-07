'''
1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example 1:

	Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
	Output: 7
	Explanation: We have various ancestor-node differences, some of which are given below :
	|8 - 3| = 5
	|3 - 7| = 4
	|8 - 1| = 7
	|10 - 13| = 3
	Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
	
Example 2:

	Input: root = [1,null,2,null,0,3]
	Output: 3
 
Constraints:

	The number of nodes in the tree is in the range [2, 5000].
	0 <= Node.val <= 105
'''

'''
注意不能设初始值为无穷，只能在有节点的时候计算
'''
# faster than 73.32% of Python3
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            cmax = cmin = node.val
            if node.left:
                lmax, lmin = dfs(node.left)
                cmax, cmin = max(cmax, lmax), min(cmin, lmin)
            if node.right:
                rmax, rmin = dfs(node.right)
                cmax, cmin = max(cmax, rmax), min(cmin, rmin)
            self.res = max(abs(node.val-cmax), abs(node.val-cmin), self.res)
            return cmax, cmin
        root and dfs(root)  
            
        return self.res