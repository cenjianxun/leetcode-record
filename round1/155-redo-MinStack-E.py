'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''
'''
重做。如果最小的移走怎么办
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def push(self, val: int) -> None:
        self.L.append(val)

    def pop(self) -> None:
        self.L.pop()
        

    def top(self) -> int:
        return self.L[-1]

    def getMin(self) -> int:
        return min(self.L)

'''
上面的那个错的。
两个方法：
1. 入栈的是一对（），存值和当前最小值
2. 另存最小值list，如果新值<=该list的最后一个值，就入栈。【！！一定要有等于】
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_nums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_nums or self.min_nums[-1] >= val:
            self.min_nums.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_nums[-1]:
            self.min_nums.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:       
        return self.min_nums[-1] 

'''
不存在删除了一个值，又再删除最小值之后，第一次被删的值成为最小值的情况，第二个相当于单调栈。所以可以用👆
且可以只用一个stack，当min变更之后，将前min存入栈；当删除最小值后，第次弹出的值为新最小值。

'''