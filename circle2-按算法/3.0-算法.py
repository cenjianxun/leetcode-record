
———————————————— NO.1  DFS  ————————————————

【DFS】
就是将所有的选择罗列出来，枚举
就是可以画出每一条可能的路径
就是可以画出决策树的就可以用dfs

🟡 dfs模板

	result = []
	def backtrack(路径, 选择列表):
	    if 满足结束条件:
	        result.add(路径)
	        return

	    for 选择 in 选择列表:
	        做选择
	        backtrack(路径, 选择列表)
	        撤销选择

1. 路径是选择列表中的其中一个选择
2. 撤销选择的意思是，本条路虽然暂时用过了这个选择，但是回溯回去这个选择还是要当没用过，所以要塞回去。
3. 动态规划的三个需要明确的点就是「状态」「选择」和「base case」，可以对应着走过的「路径」，当前的「选择列表」和「结束条件」      

子集、排列、组合可以用回溯


♻♻♻ 回溯 ♻♻♻
https://leetcode.cn/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/
DFS是一个劲的往某一个方向搜索，而回溯算法建立在DFS基础之上的，但不同的是在搜索过程中，达到结束条件后，恢复状态，回溯上一层，再次搜索。因此回溯算法与DFS的区别就是有无状态重置

· 何时使用回溯算法
当问题需要"回头"，以此来查找出所有的解的时候，使用回溯算法。即满足结束条件或者发现不是正确路径的时候（走不通），
要撤销选择，回退到上一个状态，继续尝试，直到找出所有解为止

可以用memo的回溯问题：377 416


💥 类背包问题
	🔸39 vs 40 vs 216 vs 377🔸 选数组元素使和为target
	39：都是正数。元素不重复。每个元素可无限使用。不计顺序。返回组合情况。
	40：都是正数。可有重复元素。每个元素只用一次。不计顺序=不能有不同顺序但数字一样的。返回组合情况。
	216:只能1-9。不能重复元素。必须指定个数。返回组合情况。
	377：都是正数。元素不重复。每个元素可无限使用。计顺序。返回排列个数。）

	❣去有相同数字的重必须要排序
	❣可无限使用在遍历时i 可以= start
	❣如果要去重，排序后用if i > start and nums[i] == nums[i-1]: continue
	❣如果求组合，用dfs，如果求个数，用dp
				
	39：
		无限使用的情况下，dfs的循环
		for i in range(start, Len):
			dfs(i, curlist + nums[i])
		表示可以重复使用，i可以用，可以从start开始，下一轮仍可以从i（下一轮的start）开始
	
	40：
		所以要去重。❣去有相同数字的重必须要排序❣
		但是如果数组中本来就有重复元素，这种情况下是可以用它们。
		这两种的区别是：
			在一个树上，如果是在两种情况下重复用了数字，表示在树的不同枝、同一层有重复，这就需要略过。
			如果是同种情况下用了两次该数字，就是在同一枝有重复，这个就可以。
		所以要去重不同枝但同层的：
		nums.sort() # 必须要排序！！！
		for i in range(start, Len):
			if i > start and nums[i] == nums[i-1]:
				continue
			dfs(i+1, curlist + [nums[i]])
		这里只有👆 这里的i需要+1，表示每个元素只能用一次。

	216：
		没有什么特别的

	377：



好题：306
 
———————————————— NO.2 BFS —————————————————
【BFS】 (127)

找到的路径一定是最短的，但代价就是空间复杂度比 DFS 大很多
——> step的问题多用BFS
🛑 如果step跟随当前值，而在总体里不能确定。可以将step一起放进queue。 queue = deque([(start, step)])
'''
# 从start到end
queue = Queue()
visited = set()
queue.append(start) # 起点加入队列
visited.add(start)
step = 0
while queue:
	for q in queue: # 扩散
		if q == target:
			return step
		for node in (q的相邻节点): # 将q的相邻节点加入队列
			if node not in visited:
				queue.append(node)
				visited.add(node)
	step += 1 # 更新步数
'''

双向BFS：
1. 传统的 BFS 框架就是从起点开始向四周扩散，遇到终点时停止；而双向 BFS 则是从起点和终点同时开始扩散，当两边有交集的时候停止。
2.必须知道终点在哪里


407 107 101 279 542 199 200 301 102 690 207 133 1036 787 111 130 103 515 513 127 529 417 675 310 126 210 317 505 286 490 1368 323 499 261

———————————— NO.3 差分/前缀和 ——————————————

前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。
如果我们想求区间nums[i..j]的累加和，只要计算prefix[j+1] - prefix[i]即可，而不需要遍历整个区间求和
1109
差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。
比如说，我给你输入一个数组nums，然后又要求给区间nums[2..6]全部加 1，再给nums[3..9]全部减 3，再给nums[0..4]全部加 2，再给…
构建差分数组，diff[i]意为i和i-1的差值，diff[i] += 3意思是给3及以后的都+3
所求，就是用diff反推各个值


—————————————— NO.4 union find ————————————————

主要思路是适时增加虚拟节点，想办法让元素「分门别类」，建立动态连通关系
如果需要的功能不仅仅是检测两个节点是否连通，还需要在连通时得到具体的路径，那么就需要用到别的算法了，比如DFS或者BFS。

'''
# 初始化
parent = [元素个数]
parent[i] = i   # 初始化时每个元素指向自己
size = [1] * 元素个数   # 进一步，计算权重

def union(p, q):
	# 根节点要么是p要么是q
	# parent[p] = q or parent[q] = p

	# 先找出两个节点的根
	pid, qid = find(p), find(q)

	# 如果不等就连接
	if pid != qid:
		# 进一步，判断谁权重小，小者依附
		if size[pid] > size[qid]:
			parent[qid] = pid
			size[pid] += size[qid]
		else:
			parent[pid] = qid
			size[qid] += size[pid]


def find(p):
	# 返回的是它的根节点
	while parent[p] != p: # 因为只有根节点自己指向自己
		p = parent[p]
	# if parent[p] != p: p = find(parent[p])
	return p
'''
 
———————————— NO.5 KMP ——————————————
28 459 686


—————————————— NO.6 Dijkstra & Bellman-Ford ————————————————
787

Dijkstra:解决有权无向图（maybe有向 ）  
Dijkstra 的模板：
需要一个visited，记录走过的
需要一个链表dist，记录每一个节点，从【start】到它的最短路径，初始为正无穷
需要一个graph，记录u->v以及他们的权重
每一轮：
1 筛选出目前为止，没走过的，路径最短的节点s
2 遍历以s为起点的graph，找到s->e的e，并依次比较本身e记录在dist里（即从开头到e的）最短长度+从s到e的权重w，和s的最短长度，即：
dist[s] + dist(从s到e) VS dist[e]
每多走一步，都要全部更新判断，当前每个节点在最短记录里的(从起点的)长度是不是最短，还可不可以更短

最终结束在：如果有正无穷在dist里则返回-1（无法遍历），否则返回max

--

Bellman-Ford的区别：
可以解决负权重边（但不能解决负环）
Dijkstra每次谨慎选一个最小的加入list，BF每一次都遍历所有结点
for _ in 每个顶点：
	for u, v, w in 每个边：
	#如果某次循环中，考虑每条边后都没改变最短路径，则可break
		if 新路更优：
			marked[v] = 新路
for u, v, w in 每个边：
	if 还存在一个dist[v] > dist[u] + w:
		有负环回路
	else：
		没有负环回路
 

———————————— NO.7 Kruskal & Prim —————————————— 

Kruskal：找全局里权重最小的边
prim：找已知里最小的边


———————————— NO.8 线段树 ——————————————


———————————— NO.9 其它算法 ——————————————
桶



===================================================================================

————— DFS —————
Number of Atoms	
★★★	726	
*** 736

Score of Parentheses
★★★ 856	
** 394

Generate Parentheses	
★★★	22	
*** 301	
				 

————— BFS —————
773

Word Ladder	
★★★★	127	
** 752	
*** 126	818	 

01 Matrix	
★★★	542	
** 934
*** 675					 


————— union-find —————
# union find
Evaluate Division	★★★	
399	
** 839	990	721	(737)
*** 952	



————— 回溯 —————
*** 726 736 856



advanced：
trie: 648 676 677  *** 745

BIT/Segment Tree: 307

monotonic:
239 # queue 
316 402 560 739 901 907 962 1019 1124 # stack 
*** 975

Manacher：
