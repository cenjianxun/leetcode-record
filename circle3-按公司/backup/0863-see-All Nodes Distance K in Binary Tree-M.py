'''
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
'''

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.visited = set()
        def find_in_child(node, n):
            if not node or node in self.visited:
                return 
            if n == 0:
                self.res.append(node.val)
                return 
            find_in_child(node.left, n-1)
            find_in_child(node.right, n-1)
        find_in_child(target, k)
        self.visited.add(target)
        def find_target(node):
            if not node:
                return None, -1
            if node == target:
                return node, 1
            left, lx = find_target(node.left)
            right, rx = find_target(node.right)
            if left or right:
                x = left and lx or rx
                self.visited.add(left or right)
                find_in_child(node, k-x)
                return node, 1+x
            return None, -1
        find_target(root)
        return self.res