'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

'''
细节
慢 faster than 8.79% of Python3
'''
class Node:
    def __init__(self, key=None, value=None, Next=None, pre=None):
        self.key = key
        self.value = value
        self.next = Next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dic = {}
        self.cur_p = ''
        self.head = ''
        self.valid_num = 0
        
    def get(self, key: int) -> int:
        if not key in self.cache_dic or not self.cache_dic.get(key):
            return -1
        else:
            if self.cache_dic.get(key) and self.cache_dic[key] != self.cur_p:
                self.exchange(key)
            return self.cache_dic[key].value

    def put(self, key: int, value: int) -> None:
        if self.cache_dic.get(key):
            if self.cache_dic[key] != self.cur_p:
                self.exchange(key)
            self.cache_dic[key].value = value
        else:
            node = Node(key=key, value=value)
            self.cache_dic[key] = node
            if self.cur_p:
                self.cur_p.next = node
                node.pre = self.cur_p
            if not self.head:
                self.head = node
            self.cur_p = node
            # print('pre', key, value, self.head.value, self.cur_p.value)
            if self.valid_num < self.capacity:
                self.valid_num = self.valid_num + 1
            else:
                k = self.head.key
                self.head = self.head.next
                self.head.pre = None
                self.cache_dic[k].next = None
                self.cache_dic[k] = ''
        # print(key, value, self.cache_dic[key].value, self.valid_num, self.head.value, self.cur_p.value)
            
    def exchange(self, key):
        if self.cache_dic[key] == self.head:
            self.head = self.cache_dic[key].next
        else:
            self.cache_dic[key].pre.next = self.cache_dic[key].next
        self.cache_dic[key].next.pre = self.cache_dic[key].pre
        self.cur_p.next = self.cache_dic[key]
        self.cache_dic[key].pre = self.cur_p
        self.cur_p = self.cache_dic[key] 

'''
要用双向列表的原因是，删除时间开销是1
不能用deque，需要自造的原因是，好像没实现删除的这个功能。
** 可以让双链表头和尾都指向自己，这样只用一个root，root前一个是tail, 下一个是head
'''
class Deque:
    def __init__(self, key=None, val=None, nex=None, pre=None):
        self.key = key
        self.val = val
        self.nex = nex
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.node = self.root = Deque()
 

    def get(self, key: int) -> int:
        # print('get', key)
        if key in self.map:
            node = self.map[key]
            # print(node.key, node.pre.key)
            self.del_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print('put', key, value)
        if key in self.map:
            node = self.map[key]
            self.del_node(node)  
            node.val = value
        else:
            node = Deque(key=key, val=value)

        self.map[key] = node
        self.add_node(node)
        if len(self.map) > self.capacity:
            del_node = self.root.nex
            # print(del_node.key, del_node.val)
            self.del_node(del_node)
            self.map.pop(del_node.key)
 
        # self.pprint()
    def pprint(self):
        p = self.root.nex
        l = []
        while p:
            l.append((p.key, p.val))
            p = p.nex
        # print(l)
        
    def add_node(self, node):
        if node != self.node:
            self.node.nex = node
            node.pre = self.node
            self.node = node          

    def del_node(self, node):
        if node != self.node:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            node.nex = None
            node.pre = None



class LinkNode:
    def __init__(self, val=None):
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.head = LinkNode(capacity)
        self.tail = LinkNode(0)
        self.head.next = self.tail
        self.tail.pre = self.head 
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        if node.val != -1:
            self.del_node(node)
            self.add_node(node)
        return node.val
            
    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            if node.val != -1:
                self.del_node(node)
            else:
                self.tail.val += 1
            node.val = value
        else:
            node = LinkNode(value)
            self.dict[key] = node
            self.tail.val += 1
        self.add_node(node)
        if self.tail.val > self.head.val:
            self.tail.pre.val = -1
            self.del_node(self.tail.pre)
            self.tail.val -= 1
 
        
    def add_node(self, node):
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
    
    def del_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = node.next = None
        
def pnode(node):
    stack = []
    p = node
    while p:
        stack.append(p.val)
        p = p.next
    print(stack)
    
def pdic(dic):
    stack = []
    for k in dic:
        stack.append((k, dic[k].val))
    print(stack)