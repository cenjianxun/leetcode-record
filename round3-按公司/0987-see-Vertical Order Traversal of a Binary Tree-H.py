'''
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''

'''
还可以用递归
'''
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0, 0)]
        dic = defaultdict(list)
        dic[0].append((0, root.val))
        while stack:
            temp = []
            for node, row, col in stack:
                node.left and temp.append((node.left, row+1, col-1))
                node.right and temp.append((node.right, row+1, col+1))
                node.left and dic[col-1].append((row+1, node.left.val))
                node.right and dic[col+1].append((row+1, node.right.val))
            stack = temp
            #print(stack)
            #print(dic)
        res = []
        for k in sorted(dic.keys()):
            res.append([v[1] for v in sorted(dic[k])])
        return res