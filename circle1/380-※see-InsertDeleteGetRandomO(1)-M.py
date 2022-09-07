'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
'''
1.O1删除元素可以交换最后一个
2.交换之后需要把dic值重置
'''

# faster than 35.20% of Python3 
# less than 30.61% of Python3
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_list = []
        self.nums_dic = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.nums_dic:
            # print('insert',self.nums_list, self.nums_dic)
            self.nums_list.append(val)
            self.nums_dic[val] = len(self.nums_list) - 1
            return True
        return False
    

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        i = self.nums_dic.get(val,-1)
        if i != -1:
            # if i != len(self.nums_list) - 1:
            self.nums_list[i], self.nums_list[-1] = self.nums_list[-1], self.nums_list[i]
            self.nums_dic[self.nums_list[i]] = i
            self.nums_list.pop()
            self.nums_dic.pop(val)
            
            # print('remove', self.nums_list, self.nums_dic)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # print(self.nums_list)
        '''
        # 慢
        idx = random.randint(0, len(self.nums_list)-1)
        return self.nums_list[idx]
        '''
        # faster than 63.37% of Python3
        return random.choice(self.nums_list)

        