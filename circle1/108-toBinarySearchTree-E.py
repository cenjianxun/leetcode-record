'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

'''
奇怪的解法？
# height-balanced 单词
'''

def addTree(L, root):
    i = int((len(L)-1)/2)
    left_l = L[0:i]
    right_l = L[i+1:]
    root.val = L[i]
    if left_l:
        node = TreeNode(0)
        node = addTree(left_l, node)
        root.left = node
    if right_l:
        node = TreeNode(0)
        node = addTree(right_l, node)
        root.right = node        
    return root 
    
    
def sortedArrayToBST(nums: List[int]) -> TreeNode:
    root = TreeNode(0)
    root = self.addTree(nums, root)
    return root


'''
看看递归吧
'''
# faster than 99.11% of Python3
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
if not len(nums):
    return None
if len(nums) == 1:
    return TreeNode(nums[0])
mid = int(len(nums)//2)
root = TreeNode(nums[mid])
root.left = self.sortedArrayToBST(nums[:mid])
root.right = self.sortedArrayToBST(nums[mid+1:])
return root