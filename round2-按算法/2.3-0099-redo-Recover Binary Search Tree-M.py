'''
99. Recover Binary Search Tree
Medium

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

	Input: root = [1,3,null,null,2]
	Output: [3,1,null,null,2]
	Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

	Input: root = [3,1,4,null,null,2]
	Output: [2,1,4,null,null,3]
	Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

	The number of nodes in the tree is in the range [2, 1000].
	-231 <= Node.val <= 231 - 1

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
'''

'''
二叉搜索树的精髓是：中序遍历升序。所以用中序遍历。

此外：有两种情况
① 这两个节点是兄弟，那么就要占用两个node记录，第一个node的pre和第二个node的后交换
② 这两个节点是父子，那么其实就是pre和后的关系，交换这两个
'''

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.node1 = self.node2 = None
        self.preNode = TreeNode(val=float('-inf'))
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            if self.preNode.val > node.val and not self.node1:
                self.node1 = self.preNode
            if self.preNode.val > node.val and self.node1:
                self.node2 = node
                
            self.preNode = node
            
            inorder(node.right)
        inorder(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val