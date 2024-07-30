'''
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''

'''
第一次， 
* 不能dp的原因是：dp，它前面的值都是固定的（like 二维数组只需要左和上），但是这个是不确定的，四周都需要，可能重复走。

超时
'''
from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        visited = set()
        while len(visited) < m * n:
            short, i, j = min([[cost[i][j], i, j] for i in range(m) for j in range(n) if (i,j) not in visited and cost[i][j] != float('inf')])
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and abs(heights[x][y] - heights[i][j]) < cost[x][y] and (x, y) not in visited:
                    cost[x][y] = max(cost[i][j], abs(heights[x][y] - heights[i][j]))
            visited.add((i, j))
                
        return cost[-1][-1]

'''
改进：
加heapq，
把添加进队列，移到for循环里：当cost的最小值需要更新的时候才更新

还超时
'''
from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        heap = []
        heappush(heap,(0, (0, 0)))
        while heap:
            # print(stack)
            d, (i, j) = heappop(heap)
            if (i, j) == (m-1, n-1):
                return d
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and abs(heights[x][y] - heights[i][j]) < cost[x][y] :
                    cost[x][y] = max(cost[i][j], abs(heights[x][y] - heights[i][j]))
                    heappush(heap,(cost[x][y], (x, y)))
            # visited.add((i, j))

        return cost[-1][-1]

'''
抄袭：
这个更新的判断条件合理的多：不在队列里的 or 在队列里但值比当下大的

改进：把visited和cost二维矩阵合二为一，变成一个key为坐标，value为cost值的字典
'''
from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        cost = {(0, 0): 0}
        heap = []
        heappush(heap,(0, (0, 0)))
 
        while heap:
            # print(stack)
            c, (i, j) = heappop(heap)
            if (i, j) == (m-1, n-1):
                return c
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    c = max(cost[(i,j)], abs(heights[x][y] - heights[i][j]))
                    if (x, y) not in cost or (x, y) in cost and c < cost[(x, y)]:
                        heappush(heap, (c, (x, y)))
                        cost[(x, y)] = c
        return -1

'''
或可用union find
循环找最短距离的两个点，连接成边，
最短距离逐渐+1， like step
直到起始点和目标点相连
'''