'''
307. Range Sum Query - Mutable
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
Example 1:

    Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Output
    [null, 9, null, 8]

    Explanation
    NumArray numArray = new NumArray([1, 3, 5]);
    numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
    numArray.update(1, 2);   // nums = [1, 2, 5]
    numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 
Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    0 <= index < nums.length
    -100 <= val <= 100
    0 <= left <= right < nums.length
    At most 3 * 104 calls will be made to update and sumRange.
'''

'''
这个方式建立tree的步骤：
给前面+len长度的0，然后从len-1倒着往前遍历，index0无值

parent 为i 则子树节点为 2*i和2*i+1
知道子树节点k，则par=k//2,k分奇偶，,偶左 奇右，看+1还是-1

要算总和时，如果左边界包括左子树（为偶），就直接算它的父，如果只包括右子树（为奇），就加上它的值，左边界往前+1，然后//2往父退
如果右边界包括右子树（为奇），就直接算它的父，如果只包括左子树，就加它的值，右边界-1，然后//2往父退
最终退出循环时左边界>右边界。（while里面左右相等也可以）
'''

class NumArray:
    def __init__(self, nums: List[int]):
        self.len_nums = len(nums)
        self.tree = [0] * self.len_nums + nums
        for i in range(self.len_nums - 1, 0, -1):
          # self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
          self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        index = self.len_nums + index
        self.tree[index] = val
        while index > 1:
          # self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
            self.tree[index // 2] = self.tree[index] + self.tree[(index - 1) if (index % 2) else (index + 1)]
            index //= 2
  
    def sumRange(self, left: int, right: int) -> int:
        left = self.len_nums + left
        right = self.len_nums + right
        res = 0
        while left <= right:
            if left % 2:         # if left & 1
                res += self.tree[left]
                left += 1
            left //= 2           # left >>= 1

            if not (right % 2):  # if not (right & 1)
                res += self.tree[right]
                right -= 1
            right //= 2          # right >>= 1
        return res


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)