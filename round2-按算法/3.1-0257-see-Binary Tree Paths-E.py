'''
257. Binary Tree Paths
Easy

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

	Input: root = [1,2,3,null,5]
	Output: ["1->2->5","1->3"]

Example 2:

	Input: root = [1]
	Output: ["1"]
 
Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

'''
要see的是，right 和left要一起考虑，只要有一个child，就只有一个分支而不是两个
example 1：错误答案：["1->2->5","1->3", "1->2"]
'''
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, path):
            if not node.left and not node.right:
                res.append('->'.join(path))
                return  
            if not node.left or not node.right:
                child = node.left or node.right
                path.append(str(child.val))
                dfs(child, path)
            if node.left and node.right:
                dfs(node.left, path + [str(node.left.val)])
                dfs(node.right, path + [str(node.right.val)])
        if not root:
            return []
        dfs(root, [str(root.val)])
        return res