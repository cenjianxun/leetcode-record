'''
403. Frog Jump
Hard

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.


Example 1:

	Input: stones = [0,1,3,5,6,8,12,17]
	Output: true
	Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:

	Input: stones = [0,1,2,3,4,8,9,11]
	Output: false
	Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 
Constraints:

	2 <= stones.length <= 2000
	0 <= stones[i] <= 231 - 1
	stones[0] == 0
	stones is sorted in a strictly increasing order.
'''

'''
显摆一下一遍过
'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones or stones[0] != 0:
            return False
        steps = {}
        for s in stones:
            steps[s] = set()
        steps[0] = {0}
        for s in stones:
            for k in steps[s]:
                for jump in [k-1, k, k+1]:
                    if jump > 0 and s + jump in steps:
                        steps[s+jump].add(jump)
        return bool(steps[stones[-1]])

'''
dp方法

 f[石子列表下标][上一步的的跳跃步长]
 f[i][k]可由 f[i][k-1]、f[i][k]、f[i][k+1]而来

显然，我们事先是不可能知道经过「多大的步长」跳到「哪些位置」，最终可以到达最后一块石子。

这时候需要利用「对偶性」将跳跃过程「翻转」过来分析：

我们知道起始状态是「经过步长为 1」的跳跃到达「位置 1」，如果从起始状态出发，存在一种方案到达最后一块石子的话，那么必然存在一条反向路径，它是以从「最后一块石子」开始，并以「某个步长 kk」开始跳跃，最终以回到位置 1。

因此我们可以设 f[1][1] = truef[1][1]=true，作为我们的起始值。

这里本质是利用「路径可逆」的性质，将问题进行了「等效对偶」。表面上我们是进行「正向递推」，但事实上我们是在验证是否存在某条「反向路径」到达位置 11。

'''