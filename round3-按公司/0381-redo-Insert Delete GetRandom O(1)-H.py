'''
381. Insert Delete GetRandom O(1) - Duplicates allowed

mizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also removing a random element.

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the empty RandomizedCollection object.
bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of same values the multiset contains.
You must implement the functions of the class such that each function works on average O(1) time complexity.

Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

Example 1:

	Input
	["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
	[[], [1], [1], [2], [], [1], []]
	Output
	[null, true, false, true, 2, true, 1]

	Explanation
	RandomizedCollection randomizedCollection = new RandomizedCollection();
	randomizedCollection.insert(1);   // return true since the collection does not contain 1.
	                                  // Inserts 1 into the collection.
	randomizedCollection.insert(1);   // return false since the collection contains 1.
	                                  // Inserts another 1 into the collection. Collection now contains [1,1].
	randomizedCollection.insert(2);   // return true since the collection does not contain 2.
	                                  // Inserts 2 into the collection. Collection now contains [1,1,2].
	randomizedCollection.getRandom(); // getRandom should:
	                                  // - return 1 with probability 2/3, or
	                                  // - return 2 with probability 1/3.
	randomizedCollection.remove(1);   // return true since the collection contains 1.
	                                  // Removes 1 from the collection. Collection now contains [1,2].
	randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.

Constraints:

	-231 <= val <= 231 - 1
	At most 2 * 105 calls in total will be made to insert, remove, and getRandom.
	There will be at least one element in the data structure when getRandom is called.
'''

'''
和380的区别是，380如果里面有了就不插了，381是仍然插，集合里算个数

思想就是要删除的和list里最后一个交换，再pop()最后一个
小细节真多
'''

from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.num_dict = defaultdict(set)
        self.num_list = []
        
    def insert(self, val: int) -> bool:
        
        self.num_dict[val].add(len(self.num_list))
        self.num_list.append(val)
        # 🟡 这里判断有无可以用个数判断，如果在前面判断空，又要分支key是否存在之类的
        return len(self.num_dict[val]) == 1
        
    def remove(self, val: int) -> bool:
    	# if val not in self.num_dict: ❌ 因为里面可以为空
        if not self.num_dict[val]:
            return False
        index = self.num_dict[val].pop()
        last = self.num_list[-1]
        self.num_list[index] = last
        self.num_list.pop()
        # 🟡必须先add后remove，因为add和remove的值可能是同一个，先加可以覆盖
        self.num_dict[last].add(index)
        self.num_dict[last].discard(len(self.num_list))

        return True
    
    def getRandom(self) -> int:
        return random.choice(self.num_list)