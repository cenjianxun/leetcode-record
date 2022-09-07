'''
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''

# faster than 8.59% of Python3
# less than 6.03% of Python3
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    may_can = set()
    for i in range(len(gas)):
        if gas[i] >= cost[i]:
            may_can.add(i)
    if not may_can:
        return -1
    for s in may_can:
        remain_gas = 0
        temp_gas = gas[s:] + gas[:s+1]
        temp_cost = cost[s:] + cost[:s+1]
        # print(s, temp_gas)
        # print(s, temp_cost)
        for i in range(len(temp_gas)):
            remain_gas = remain_gas + temp_gas[i] - temp_cost[i]
            # print(temp_gas[i],temp_cost[i], remain_gas)
            if remain_gas < 0:
                break
        if remain_gas >= 0:
            return s
    return -1


'''
1. 如果总cost > 总gas，就return -1 # 提升至  faster than 19.30% of Python3
2. 如果累计的剩余量<0，就从下一个重新记算
3. 之所以不用算到再折回去的部分，是因为只用考虑开始的地方，而开始的地方只有len(nums)种情况，遍历就行了。
是因为在总gas充足的情况下，假设是start，start之前都不行=>之前不足，而start可以=start到末尾充足=>start充足的量可以覆盖之前的不足
'''

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    start = sums = 0
    
    for i in range(len(gas)):
        sums = sums + gas[i] - cost[i]
        if sums < 0:
            start = i + 1
            sums = 0
    return start if sum(gas) >= sum(cost) else -1