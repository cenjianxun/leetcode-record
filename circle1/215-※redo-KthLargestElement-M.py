'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

'''
复习排序
'''

# def findKthLargest(nums: List[int], k: int) -> int:
#     nums.sort(reverse=True)
#     return  nums[k-1]

'''
用大顶堆排序
'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    # 将每个父节点的值置成父子间值最大的，直到它没有子节点
    def shift_down(array, start, end):
        while True:
            # 堆的精髓就是第i个节点的左右子树是i * 2 + 1，i * 2 + 2
            child = start * 2 + 1
            # 如果没有子节点就跳出
            if child > end:
                break
            # 是要把最大的放在父，所以比较左右子树，选更大的跟父节点交换
            if child + 1 <= end and array[child+1] > array[child]:
                child = child + 1
            if array[start] < array[child]:
                array[start], array[child] = array[child], array[start]
                # 交换之后以child为父节点的才可能又不是大顶堆，所以才需要又循环，否则就不用了就退出
                start = child
            else:
                break
    # 从长度一半-1开始往前，每个值运作一次，因为从这个值开始，它就有可能有子节点       
    start = len(nums)//2 - 1

    # 要从后（中间）往前交换，因为先交换较为叶子的部分，越往前对应的树越靠近根，就会又刷一遍之前的节点。如果反过来遍历就覆盖不到。
    for i in range(start, -1, -1):
        shift_down(nums, i, len(nums) - 1)
    
    '''
    至此为止只完成了父子节点直接的大小排序，对于本节点的子们和邻节点的子们之间的大小覆盖不到.
    例子[3,2,3,1,2,4,5,5,6]，到这里会变成[6, 5, 5, 3, 2, 4, 3, 2, 1]
    所以还需要下面的：
    '''

    # 这里循环的意思是，倒叙，逐个把最大的最顶的值和最后一个值交换，最后一个值就最大了就定了，然后再用余下的数组再调用换大顶函数一次，从0开始只一次，保证调用完之后根是剩下这些里面最大的。循环。
    for i in range(len(nums)-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        shift_down(nums, 0, i - 1)
        # 如果不是本题，就不需要下面两行，直接遍历完。注意本循环是倒着循环的，所以要用总长减。
        if len(nums) - i == k:
            return nums[i]
    # 上面那个遍历是排除了第一个数的，所以没返回到就是它
    return nums[0]    

'''
堆方法：
'''
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]
