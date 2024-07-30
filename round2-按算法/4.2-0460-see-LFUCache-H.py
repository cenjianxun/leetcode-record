'''
460. LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''

'''
多维护一个freq的字典，元素为：
  5 <-> 3 <-> 2
pre <-> node <-> next
freq:[当前freq的第一个node, freq小于当前freq的最大的的第一个node]
注意边界条件：
1.当容量为0时
2.因为0：tail也在该字典里，涉及的需要排除
3.删除node时，①当前freq存在/不存在
             ②是/不是当前freq的第一个元素。注意prefreq的第二个元素
4.增添node时，②当前freq存在/不存在
            ②是/不是当前freq的第一个元素。注意prefreq的第二个元素

'''
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 0

class LFUCache:

    def __init__(self, capacity: int):
        self.valCache = {}
        self.head, self.tail = Node(val=capacity), Node(val=0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.freqCache = {0:[self.tail]}

    def get(self, key: int) -> int:
        # print('get', key)
        if not key in self.valCache:
            return -1
        node = self.valCache[key]
        nextFreq = self.delNode(node)
        node.freq += 1
        self.addNode(node, nextFreq)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        # print('put', key,value, self.valCache.keys(), self.freqCache.keys())
        # pdic(self.freqCache)
        # pnode(self.head)
        if key in self.valCache:
            node = self.valCache[key]
            node.val = value
            nextFreq = self.delNode(node)
        else:
            node = Node(key=key, val=value)
            if self.head.val and len(self.valCache) == self.head.val:
                self.delNode(self.tail.prev)
            nextFreq = 1 if 1 in self.freqCache else 0
        if len(self.valCache) < self.head.val:
            node.freq += 1
            self.addNode(node, nextFreq)
        
            
    def delNode(self, node):      
        # print('del', node.key,node.val, node.freq, self.freqCache.keys()) 
        nextFreq = node.freq
        freq = self.freqCache[node.freq]
        if node == freq[0]:
            if node.next.freq == node.freq:
                self.freqCache[node.freq][0] = node.next
                if node.prev.freq and node.prev.freq in self.freqCache:
                    self.freqCache[node.prev.freq][1] = node.next
            else:
                if node.prev.freq and node.prev.freq in self.freqCache:
                    self.freqCache[node.prev.freq][1] = freq[1]
                del self.freqCache[node.freq]
                nextFreq = freq[1].freq
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None
        del self.valCache[node.key]
        # pnode(self.head)
        return nextFreq
        
    def addNode(self, node, nextFreq):
        # print('add', node.key, node.val, node.freq, nextFreq)
        # if node.key in (2, 3, 4, 6):
        #     pdic(self.freqCache)
        self.valCache[node.key] = node
        if node.freq in self.freqCache:
            nextNode = self.freqCache[node.freq][0]     
            self.freqCache[node.freq][0] = node
        else:
            nextNode = self.freqCache[nextFreq][0]
            self.freqCache[node.freq] = [node, nextNode]
        prevFreq = nextNode.prev.freq
        if prevFreq and prevFreq in self.freqCache:
            self.freqCache[prevFreq][1] = node
        nextNode.prev.next = node
        node.prev = nextNode.prev
        node.next = nextNode
        nextNode.prev = node