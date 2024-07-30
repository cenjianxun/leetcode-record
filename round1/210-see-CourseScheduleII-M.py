'''
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    degree = defaultdict(int)
    for u, v in prerequisites:
        graph[v].append(u)
        degree[u] = degree[u] + 1
     
    res = list(set([i for i in range(numCourses)]) - set(degree.keys()))
    flag = 0
    for i in range(numCourses):
        if not graph:
            break
        for v in graph:
            if not v in degree:
                flag = 1
                break
        if not flag:
            return []
        for u in graph[v]:
            degree[u] = degree[u] - 1
            if degree[u] == 0:
                degree.pop(u)
                res.append(u)
        graph.pop(v)
        flag = 0
    return res