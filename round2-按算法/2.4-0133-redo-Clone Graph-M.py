'''
133. Clone Graph
Medium

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

	For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

	An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

	The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

	Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
	Output: [[2,4],[1,3],[2,4],[1,3]]
	Explanation: There are 4 nodes in the graph.
	1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
	2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
	3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
	4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

	Input: adjList = [[]]
	Output: [[]]
	Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
	Example 3:

	Input: adjList = []
	Output: []
	Explanation: This an empty graph, it does not have any nodes.
 
Constraints:

	The number of nodes in the graph is in the range [0, 100].
	1 <= Node.val <= 100
	Node.val is unique for each node.
	There are no repeated edges and no self-loops in the graph.
	The Graph is connected and all nodes can be visited starting from the given node.
'''

'''
图遍历 两种 dfs，bfs

不会
'''

'''
dfs

用class 好优雅！！！

1. 用【全局】visited标记已遍历过的node
2. node和clone_node要一一对应，故此用dict
3. 迭代的部分在neigh的地方
'''
class Solution:
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node
 
'''
bfs
需要queue
记得每一个nei的hash要加入clone的neighbors
'''
class Solution:  
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if not node:
            return node
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    queue.append(nei)
                    visited[nei] = Node(nei.val, [])
                visited[n].neighbors.append(visited[nei])
        return visited[node]

