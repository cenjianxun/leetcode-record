'''
1381. Design a Stack With Increment Operation
Medium
 
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
'''

'''
要O(1)解决，要多一个list记录偏移量（increment），等到pop的时候再加这个offset

注意的是offset数组的边界，它是否为空，是否超size
'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.offset = []

    def push(self, x: int) -> None:
        
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.offset.append(0)
        #print('push', self.stack, self.offset)

    def pop(self) -> int:
        
        if self.stack:
            incre = self.offset.pop()
            if self.offset:
                self.offset[-1] += incre
            #print('pop',self.stack, self.offset, incre)
            return self.stack.pop() + incre
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        #print(k, val, self.stack)
        index = min(k - 1, len(self.stack) - 1)
        if index > - 1:
            self.offset[index] += val