'''
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# faster than 52.31% of Python3
def flatten( root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    p = root
    while p:
        # print(p.val)
        if p.left:
            self.left_to_right(p)
        else:
            p = p.right
        
def left_to_right(self, p):
    # print(p.val, p.left.val, p.right.val)
    left = p.left
    while left.right:
        left = left.right
    left.right = p.right
    p.right = p.left
    p.left = None