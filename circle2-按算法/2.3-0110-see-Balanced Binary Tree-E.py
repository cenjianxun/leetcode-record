'''
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 
Example 1:

	Input: root = [3,9,20,null,null,15,7]
	Output: true

Example 2:

	Input: root = [1,2,2,3,3,null,null,4,4]
	Output: false

Example 3:

	Input: root = []
	Output: true

Constraints:

	The number of nodes in the tree is in the range [0, 5000].
	-104 <= Node.val <= 104
'''

'''
自己做的 为什么这么麻烦
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        def dfs(node):
            if not node:
                return True
            left = depth(node.left)
            right = depth(node.right)
            if abs(left-right) > 1:
                return False
            return dfs(node.left) and dfs(node.right)
            
        return dfs(root)

'''
改成不用dfs
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
 
        return abs(depth(root.left)-depth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

'''
👆自顶向下👆和👇自底向上👇

其实感觉重点不是自哪向哪，而且也没看出来怎么自了。感觉关键是，返回值可以同时表示高度和是否平衡
正数就是平衡且有高度，-1就是不平衡

噢看出来了
👆是再return的时候先判断本node（用abs），再分别判断left和right（用isBalance）
👇是在helper里面先判断left和right，再计算本node的高度
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            if left == -1:
                return -1
            right = helper(node.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1
        return helper(root) != -1