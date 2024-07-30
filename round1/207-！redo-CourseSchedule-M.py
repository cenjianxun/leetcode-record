'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    degree = defaultdict(int)
    for u, v in prerequisites:
        degree[u] = degree[u] + 1
        graph[v].append(u) 
    flag_0 = 0
    for v in range(numCourses):
        if not  graph:
            return True
        for i in graph:
            if not degree.get(i) :
                print(i)
                flag_0 = 1
                break

        if not flag_0:
            return False
        for j in graph[i]:
            degree[j] = degree[j] - 1
        graph.pop(i)
        flag_0 = 0
    return True

'''
dfs怎么快这么多
'''
#  faster than 97.20% of Python3
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}#defaultdict(list)
        for u, v in prerequisites:
            if v not in graph:
                graph[v] = [u]
            else:
                graph[v].append(u)
        self.visited = [-1] * numCourses
        
        for v in graph:
            if self.dfs(v, graph):
                return False
        return True
    
    def dfs(self, v, graph):
        flag = 0
        self.visited[v] = 0
        if v in graph:
            for u in graph[v]:
                if self.visited[u] == -1:
                    flag = self.dfs(u, graph)
                if flag or self.visited[u] == 0:
                    return 1
        self.visited[v] = 1
        return 0


'''
220617
查找有向图中有无环：拓扑排序
https://blog.csdn.net/weixin_42939835/article/details/108737511

bfs: 
起点是入度为0的那些点，就是没有进入它的点，with list
然后将这些点的出度点的个数减1. so需要记录：
① 所有点：它指向的点的映射关系with map
② 所有点入度的个数with map
需要记录哪些点已经走过了，用visited (set) 也可以，用入度个数标为-1也可以
当没有入度为0的点时跳出循环。
判定：如果没有环，则会刚好用N次，也没有入度为0的点了。如果不满足这个，就是有环。
'''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].add(u)
            indegree[u] += 1
        zero = [i for i in range(len(indegree)) if not indegree[i]]
        while zero:
            for v in zero:
                numCourses -= 1
                indegree[v] -= 1
                for u in graph[v]: 
                    indegree[u] -= 1
            #print(zero, indegree)
            zero = [i for i in range(len(indegree)) if not indegree[i]]
        return numCourses == 0

'''
dfs: 
仍然需要入点和出点关系的映射with map
需要visited记录。此时有三种情况：没遇到的，正在当前点这条线儿上的，已经遍历完且安全无环的。
判断：如果当前的点指向的点，又遇到了正在当前点这条线儿上的，就说明有环。如果遇到已经安全的，就说明此点也安全
！遍历时，可以遍历N，也可以遍历初始graph的key，注意当遍历graph时，后续要判定这个key的value在不在这个graph的key里，因为defaultdict会自动添加。
'''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for u, v in prerequisites:
            graph[v].add(u)
        # -1:还没visit，0:正在visit，1:visit过了且安全
        self.visited = [-1] * numCourses
        print(graph)
        for v in graph:
            if not self.dfs(v, graph):
                return False
        return True
            
 
    def dfs(self, v, graph):
        if self.visited[v] == 0:
            return False
        if v not in graph or self.visited[v] == 1:
            return True
        self.visited[v] = 0

        for u in graph[v]:
            if not self.dfs(u, graph):
                return False    
        self.visited[v] = 1
        return True