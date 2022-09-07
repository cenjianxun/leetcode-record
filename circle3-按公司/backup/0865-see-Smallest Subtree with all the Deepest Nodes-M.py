'''
865. Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
'''

'''
题意好难理解：
有最深的叶结点的最近的共同祖先=> 意思就是只返回一个node，它包含所有含有最深节点的节点

关键点其实是
1. defaultdict(lambda:defaultdict(set))
2. set的remove和pop
'''
# faster than 88.10% of Python3
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        count = defaultdict(lambda:defaultdict(set))
        def countdeep(node, layer):
            if not node:
                return layer - 1
            left = countdeep(node.left, layer+1)
            right = countdeep(node.right, layer+1)
            max_deep = count.keys() and max(count.keys()) or 0
            if left >= right and left >= max_deep:
                count[left][left-layer-1].add(node.left)
            if left <= right and right >= max_deep:
                count[right][right-layer-1].add(node.right)
            return max(left, right)
        deepest = countdeep(root, 1)
        count[deepest][deepest-1].add(root)
        key = 0
        res = count[deepest][key]
        while len(res) > 1:
            key += 1
            temp = set()
            for node in count[deepest][key]:
                if node.left and node.left in res or node.right and node.right in res:
                    temp.add(node)
            res = temp
        return res.pop()

'''
无语！！！
为什么不直接返回node
'''
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return node, 0
            left, left_layer = dfs(node.left)
            right, right_layer = dfs(node.right)
            if left_layer == right_layer:
                return node, left_layer + 1
            if left_layer > right_layer:
                return left, left_layer + 1
            if right_layer > left_layer:
                return right, right_layer + 1
        node, layer = dfs(root)
        return node