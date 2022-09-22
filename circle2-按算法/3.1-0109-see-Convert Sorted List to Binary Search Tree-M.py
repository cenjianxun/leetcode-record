'''
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

'''
要单独看head.next存不存在的情况
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            node = TreeNode(head.val)
            return node
        pre = None
        pre.next = head
        fast = slow = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        
        next_ = slow.next
        pre.next = slow.next = None
        
        node = TreeNode(slow.val)
        #print(root.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(next_)
        return node