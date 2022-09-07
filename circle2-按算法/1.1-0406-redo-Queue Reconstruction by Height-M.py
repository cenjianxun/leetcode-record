'''
406. Queue Reconstruction by Height
Medium

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:

	Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
	Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
	Explanation:
	Person 0 has height 5 with no other people taller or the same height in front.
	Person 1 has height 7 with no other people taller or the same height in front.
	Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
	Person 3 has height 6 with one person taller or the same height in front, which is person 1.
	Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
	Person 5 has height 7 with one person taller or the same height in front, which is person 1.
	Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:

	Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
	Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]] 

Constraints:

	1 <= people.length <= 2000
	0 <= hi <= 106
	0 <= ki < people.length
	It is guaranteed that the queue can be reconstructed.
'''

'''
好慢
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res, preNo = [], {}
        for h, no in people:
            if no not in preNo:
                preNo[no] = []
            preNo[no].append([h, no])
            
        res.extend(sorted(preNo[0]))
                                
        for i in range(1, max(preNo) + 1):
            if i not in preNo:
                continue
            for h, no in preNo[i]:
                j, heigher = 0, 0
                while j < len(res):
                    if res[j][0] >= h:
                        heigher += 1
                    if heigher > i:
                        break
                    j += 1
                res.insert(j, [h, no])
                #print(h, no, res)
        return res

'''
此题的贪心策略：

遇到两个维度权衡的时候，一定要先确定一个维度，再确定另一个维度。
如果两个维度一起考虑一定会顾此失彼。

本题：

如果按照k来从小到大排序，排完之后，会发现k的排列并不符合条件，身高也不符合条件，两个维度哪一个都没确定下来。

那么按照身高h来排序呢，身高一定是从大到小排（身高相同的话则k小的站前面），让高个子在前面。

因此先以h排序

then只需要按照k为下标重新插入队列就可以了

按照身高排序之后，优先按身高高的people的k来插入，后序插入节点也不会影响前面已经插入的节点，最终按照k的规则完成了队列。

所以在按照身高从大到小排序后：

局部最优：优先按身高高的people的k来插入。插入操作过后的people满足队列属性

全局最优：最后都做完插入操作，整个队列满足题目队列属性

局部最优可推出全局最优，找不出反例，那就试试贪心。
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        print(people)
        for p in people:
            res.insert(p[1], p)
        return res