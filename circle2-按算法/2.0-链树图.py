———————————————— NO.1  哈希表 ———————————————— 

使用哈希表优化时间复杂度 

697：在遍历的时候，可以使用map来记录每个值第一次和最后一次出现的index


———————————————— NO.2  堆 & 链表 ———————————————— 

堆:
295 logN求中值，大顶堆+小顶堆，存前半部分和后半部分
480 692 215 373  973 
218 天际线问题：https://leetcode.cn/problems/the-skyline-problem/solution/gong-shui-san-xie-sao-miao-xian-suan-fa-0z6xc/

23 407 264 218 215 313 347 378 778 295 355 239 719 659 451 373 502 692 253 358

———————————————— NO.3   树 ———————————————— 

· 一个难点就是，如何把题目的要求细化成每个节点需要做的事情。
· 相信这个定义，而不要跳进递归细节

BST 二叉搜索树：
· 左子树<根<右子树
· 中序遍历结果是有序的（升序）
* 合法性：整个左树都要小，而不是只它的左子树比它小
* 如果在bst里比较或查找，可以利用它有序的特性，在普通树（中序）遍历的基础上，每一步作比较剪枝
· 如果当前节点会对下面的子节点有整体影响，可以多传递几个参数，借助参数传递信息
  → 看下左子树和右子树需要处理的步骤是不是相同，如果相同用一个就好了

 

95 94 96 226 104 108 617 107 543 114 105 101 687 654 655 449 199 257 102 144 669 538 124 112 145 501 100 530 222 111 637 437 173 337 653 404 110 776 99 863 103 563 684 235 515 297 236 513 606 652 113 106 508 230 129 662 783 98 572 671 450 250 685 623 116 998 255 333 1008 117 988 270 549 582 156 285 272 666 366 536 545 298 331

字典树：676

———————————————— NO.5  图 ———————————————— 
419？ 54 750

对角线上的点(x, y)满足一个性质：x + y == i

https://bbs.huaweicloud.com/blogs/342362

如果图包含环，需要visited数组做辅助。visited数组的操作很像回溯算法做「做选择」和「撤销选择」，区别在于位置，回溯算法的「做选择」和「撤销选择」在for循环里面，而对visited数组的操作在for 循环外面。
为什么回溯算法框架会用后者？因为回溯算法关注的不是节点，而是树枝，不信你看 回溯算法核心套路 里面的图，它可以忽略根节点。

显然，对于这里「图」的遍历，我们应该把visited的操作放到 for 循环外面，否则会漏掉起始点的遍历。

当然，当有向图含有环的时候才需要visited数组辅助，如果不含环，连visited数组都省了，基本就是多叉树的遍历。
'''
图的遍历结构：
# 如果是无环图，就没有visited那两行
def traverse(graph, point):
	if visited[point]:
		return
	visited[point] = True
	for (TreeNode neighbor : graph.neighbors(s)):
		traverse(neighbor)
	visited[point] = False
'''

拓扑排序：
就是先来的先完成才能完成后来的（选课）
拓扑排序的基础是后序遍历。
后序遍历的这一特点很重要，之所以拓扑排序的基础是后序遍历，是因为一个任务必须在等到所有的依赖任务都完成之后才能开始开始执行。

有向环需要三个点标记的原因：
因为第二次遇到同一个点有两种情况：
1.它结束了（合法到结尾但不是环，when a和b都指向c的时候）
2.成环了
所以需要不同的id区别这两种情况
https://cs.stackexchange.com/questions/9676/the-purpose-of-grey-node-in-graph-depth-first-search

https://bbs.huaweicloud.com/blogs/342362

399 207 133 332 684 310 210 685 269 444 323 261
————————————————————————————————————————————————————————————————————————————————————————————————


数组：
Design Linked List	
★★★★ 707	


Koko Eating Bananas	
★★★ 875	
** 1011

Kth Smallest Element in a Sorted Matrix	
★★★★	378	
*** 668

Find K-th Smallest Pair Distance	
★★★★	719	
*** 786
		

树：
Binary Tree Maximum Path Sum	★★★	 
*** 124	
 
Binary Tree Pruning		★★★ 
** 814  1325	

Serialize and Deserialize Binary Tree	★★★ 
297	
** 449	

Binary Tree Cameras	★★★★	 
*** 968	
** 337	979

Find Mode in Binary Search Tree	★★★	
# inorder
** 501				

Delete Node in a BST	★★★★
# binary search
** 450				

# Kruskal Prim
 1135 1584

图：
# grid + connected components
Number of Islands	★★	
200	
** 547	695	 1162	
*** 827	

# DFS, connected components
Keys and Rooms	★★					
** 841	1202

# topology sorting	
Course Schedule	★★★
207		
** 210	802		

# bipartition, graph coloring
Is Graph Bipartite?	★★★
785	
** 886	1042			

# in/out degrees	
Find the Town Judge	★★★				
997	

# unweighted shortest path / BFS
Minimum Genetic Mutation	★★★	
433	
** 863	1129	
*** 815	1263		

# cycle, union find
Redundant Connection	★★★★	
684	
** 1319
*** 685	

# weighted shortest path
Network Delay Time	★★★★	
743	
** 787	1334	
*** 882	924	

# BFS
Shortest Path Visiting All Nodes ★★★★			
	
*** 847 864	1298	

# union find / grid + CCs
Regions Cut By Slashes	★★★★★			
959				

# Dijkstra 
** 505 743 1514 1631
*** 882 


# Eulerian path
Reconstruct Itinerary	★★★★		
332					

# Tarjan
Critical Connections in a Network
★★★★						
1192	

# Hamiltonian path (DFS / DP)
Find the Shortest Superstring	★★★★★
943	
*** 980	996			

