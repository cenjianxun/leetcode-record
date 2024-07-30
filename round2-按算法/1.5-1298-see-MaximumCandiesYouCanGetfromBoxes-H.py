'''
1298. Maximum Candies You Can Get from Boxes

Given n boxes, each box is given in the format [status, candies, keys, containedBoxes] where:

status[i]: an integer which is 1 if box[i] is open and 0 if box[i] is closed.
candies[i]: an integer representing the number of candies in box[i].
keys[i]: an array contains the indices of the boxes you can open with the key in box[i].
containedBoxes[i]: an array contains the indices of the boxes found in box[i].
You will start with some boxes given in initialBoxes array. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.
'''

'''
其他方法：如果没有任何可以开的🔒就退出。
'''

from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        numsOfCandies = 0
        stack = deque(initialBoxes)
        last_stack = []
        while stack != last_stack:
            s = len(stack)
            last_stack = stack.copy()
 
            for _ in range(s):
                index = stack.popleft()
  
                if status[index] == 1:
                    numsOfCandies += candies[index]
                    status[index] = -1
                elif status[index] == 0:
                    stack.append(index)
                for i in keys[index]:
                    if status[i] == 0:
                        status[i] = 1
                for i in containedBoxes[index]:
                    stack.append(i)
 
        return numsOfCandies