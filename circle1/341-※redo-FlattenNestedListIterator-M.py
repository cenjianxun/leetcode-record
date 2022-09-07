'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# faster than 83.62% of Python3
# less than 41.88% of Python3 
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
    
    def next(self) -> int:
        return self.nestedList.pop(0).getInteger()
    
    def hasNext(self) -> bool:

        while len(self.nestedList) and not self.nestedList[0].isInteger():
            n = self.nestedList.pop(0)
            self.nestedList = n.getList() + self.nestedList  
            
        return len(self.nestedList)

# ?

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.tempIter = iter(nestedList)
        self.temp = self.getNext()
        
    def next(self) -> int:
        res = self.temp
        self.temp = self.getNext()
        print('r', res, self.temp)
        return res
    
    def hasNext(self) -> bool:
        
        return self.temp != None
        
    def getNext(self):
        
        while self.tempIter or self.stack:
            print('g', self.tempIter, self.stack) 
            if self.tempIter:
                print('?')
                n = next(self.tempIter)
                print('n', n.isInteger(), self.stack)
                if n.isInteger():
                    t = n.getInteger()
                    print(t)
                    return t
                else:
                    self.stack.append(self.tempIter)
                    self.tempIter = iter(n.getList())     
            else:
                print('nt', self.tempIter)
                self.tempIter = self.stack.pop(0) 
        return 