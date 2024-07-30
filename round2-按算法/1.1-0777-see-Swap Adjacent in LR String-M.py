'''
777. Swap Adjacent in LR String
Medium

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

	Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
	Output: true
	Explanation: We can transform start to end following these steps:
	RXXLRXRXL ->
	XRXLRXRXL ->
	XRLXRXRXL ->
	XRLXXRRXL ->
	XRLXXRRLX

Example 2:

	Input: start = "X", end = "L"
	Output: false
 
Constraints:

	1 <= start.length <= 104
	start.length == end.length
	Both start and end will only consist of characters in 'L', 'R', and 'X'.
'''

'''
我醉了竟然错了那么多次

注意 L for第一个和 R for最后一个
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        # RX->XR, XL->LX
        start_range, end_pos = [], []
        pre = 0
        for i in range(len(start)):
            if start[i] != 'X':
                start_range.append([start[i], i, i])
            if end[i] != 'X':
                end_pos.append((end[i], i))
                
        if len(start_range) != len(end_pos):
            return False
        
        for i in range(len(start_range)):
            if start_range[i][0] == 'L':
                if i > 0:
                    start_range[i][1] = start_range[i-1][1] + 1
                else:
                    start_range[i][1] = 0
                    
        for i in range(len(start_range) - 1, -1, -1):
            if start_range[i][0] == 'R':
                if i < len(start_range) - 1:
                    start_range[i][2] = start_range[i+1][2] - 1
                else:
                    start_range[i][2] = len(start) - 1


        # print(start_range)
        # print(end_pos)
        while start_range:
            # print(start_range)
            # print(end_pos)
            s, left, right = start_range.pop()
            e, index = end_pos.pop()
            if s != e:
                return False
            if index > right or index < left:
                return False
        return True