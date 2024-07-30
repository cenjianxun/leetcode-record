'''
919. Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
TreeNode get_root() Returns the root node of the tree.
'''


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.treelist = self.insert_tree(root)
        
    def insert(self, val: int) -> int:
        index = len(self.treelist)
        node = TreeNode(val)
        self.treelist.append(node)
        if not index:
            return
        if index%2:
            par = (index-1)//2
            self.treelist[par].left = node
        else:
            par = index//2 - 1
            self.treelist[par].right = node
        return self.treelist[par].val           

    def get_root(self) -> Optional[TreeNode]:
        return self.treelist[0]
 
    def insert_tree(self, tree):
        stack = [tree]
        start, end = 0, len(stack)
        while start < end:
            for i in range(start, end):
                node = stack[i]
                node.left and stack.append(node.left)
                node.right and stack.append(node.right)
            start = end 
            end = len(stack)
        return stack