'''
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''


'''
如果visited 只放src节点会超内存，如果放(s,d)会出错
res 放(s, d)会超时
'''
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for s, d, p in flights:
            graph[s].add((d, p))
        #print(graph)
        queue = deque([(src, 0, 0)])
        res = {}
        while queue:
            s, price, stop = queue.popleft()
            if stop <= k:
                for d, p in graph[s]:
                    if (d, s) not in res:
                        if (s, d) not in res:
                            res[(s, d)] = price + p
                        else:
                            res[(s, d)] = min(res[(s, d)], price + p)
                        queue.append((d, res[(s, d)], stop + 1))
        return res.get((src, dst), -1)

'''
超内存
'''

from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for s, d, p in flights:
            graph[s].add((d, p))
        #print(graph)
        queue = deque([(src, 0, 0)])
        res = float('inf')
        while queue:
            s, price, stop = queue.popleft()
            if stop <= k and price < res:
                for d, p in graph[s]:
                    if d == dst:
                        res = min(res, p + price)
                    else:
                        queue.append((d, p + price, stop+1))
        return -1 if res == float('inf') else res



'''
要按每一层循环，但list会变，可以使用：先记录list的长度，在range(len)里的list就可以append了。
但还是超内存
'''
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for s, d, p in flights:
            graph[s][d] = p
        queue, step = deque([(src, 0)]), 0
        res = float('inf')
        while queue:

            size = len(queue)
            for i in range(size):
                cur, cost = queue.popleft()
                if cur == dst:
                    res = min(res, cost)
                for d, p in graph[cur].items():
                    if cost + p <= res:
                        queue.append((d, p + cost))
            if step > k:
                break
            step += 1

        return -1 if res == float('inf') else res

'''
唯一成功的

有三个判断，k，dst，还有一个如果当前花费已经比存的res大，就抛弃。这个一开始忘了

然后只有比res小的入队列。那么初始res需要小技巧：lambda: float('inf')
'''
# faster than 99.79% of Python3
from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(set)
        for s, d, p in flights:
            graph[s].add((d, p))
        #print(graph)
        queue = deque([(src, 0, -1)])
        res = defaultdict(lambda: float('inf'))
        while queue:
            s, price, stop = queue.popleft()
            if s == dst or stop == k:
                continue
            for d, p in graph[s]:
                if price + p < res[d]:
                    res[d] = price + p
                    queue.append((d, res[d], stop + 1))
        return res.get(dst, -1)