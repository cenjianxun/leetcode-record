'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

'''
m是浮点数不能进[i]
是减1，不是加1
'''
# faster than 8.31% of Python3
import bisect
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.nums, num)
        
    def findMedian(self) -> float:
        if not self.nums:
            return
        m = len(self.nums)/2
        if m == int(m):
            return (self.nums[int(m)] + self.nums[int(m)-1])/2
        else:
            return self.nums[int(m)]
        # median = (self.data[l//2] + self.data[(l-1)//2])/2.0


'''
中位可用用大顶堆+小顶堆
'''
# faster than 27.24% of Python3
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
 

    def addNum(self, num: int) -> None:
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.max_heap, -1 * num)
        else:
            if len(self.max_heap) == len(self.min_heap):
                if num > self.min_heap[0]:
                    num = heapq.heappushpop(self.min_heap, num)
                heapq.heappush(self.max_heap, -1 * num)
            else:
                if num < -1 * self.max_heap[0]:
                    num = -1 * heapq.heappushpop(self.max_heap, -1 * num)
                heapq.heappush(self.min_heap, num)             
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-1 * self.max_heap[0] + self.min_heap[0])/2 
        else:
            return -1 * self.max_heap[0]

    # def addNum(self, num):
    #     if len(self.small) == len(self.large):
    #         heappush(self.large, -heappushpop(self.small, -num))
    #     else:
    #         heappush(self.small, -heappushpop(self.large, num))

    # def findMedian(self):
    #     if len(self.small) == len(self.large):
    #         return float(self.large[0] - self.small[0]) / 2.0
    #     else:
    #         return float(self.large[0])


'''
普通地超时
'''
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    def addNum(self, num: int) -> None:
        while self.left and self.left[-1] > num:
            self.right.append(self.left.pop())
        while self.right and self.right[-1] < num:
            self.left.append(self.right.pop())
        self.right.append(num)
        while len(self.right) > len(self.left):
            self.left.append(self.right.pop())
        while len(self.left) - len(self.right) > 1:
            self.right.append(self.left.pop())
        #print(num, self.left, self.right)
 

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[-1]+self.right[-1])/2
        else:
            return self.left[-1]


'''
heapq是小顶堆
num = heapq.heappushpop(heap, num) 意思是替换出来

不用先比较num，如果该放入small，就先放入large搅弄一番，反之。
'''

import heapq
class MedianFinder:
    def __init__(self):
        self.smallhp = []
        self.largehp = []
        
    def addNum(self, num: int) -> None:
        if len(self.largehp) == len(self.smallhp):
            num = -heapq.heappushpop(self.smallhp, -num)
            heapq.heappush(self.largehp, num)
        else:
            num = heapq.heappushpop(self.largehp, num)
            heapq.heappush(self.smallhp, -num)
        #print(self.smallhp, self.largehp)  
        
    def findMedian(self) -> float:
        if len(self.smallhp) == len(self.largehp):
            res = (self.largehp[0] - self.smallhp[0])/2
        else:
            res = self.largehp[0]
        #print(res)
        return res