'''
552. Student Attendance Record II
Hard

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

Example 1:

	Input: n = 2
	Output: 8
	Explanation: There are 8 records with length 2 that are eligible for an award:
	"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
	Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:

	Input: n = 1
	Output: 3
	Example 3:

	Input: n = 10101
	Output: 183236316

Constraints:

	1 <= n <= 105
'''

'''
这道题有两个点
1. 怎么表示当前的值
	dp[i][P] = dp[i-1][p] + dp[i-1][l] + dp[i-1][a]

	# L的前提是不要之前有连着的两个L，所以要的是上一层P和A结尾的 + 上上层P和A结尾的
	xxxPP，xxxLP，xxxAP，xxxPA，xxxLA，xxxAA || xxxP，xxxA 
	本来是(xxxPP，xxxLP，xxxAP)，(xxxPL，xxxLL， xxxAL),       (xxxPA，xxxLA，xxxAA) - xxxLL
			dp[i-1][p]         dp[i-2][p]      dp[i-2][a]    dp[i-1][a]
	dp[i][L] = dp[i-1][p] + dp[i-1][a] + dp[i-2][p] + dp[i-2][a]

	# A的前提是不要之前出现过A的
	dp[i][A] = dpNA[i-1][0] + dpNA[i-1][1] 


2. 初始化
index=0时， presnt都是1，其它是0
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        # 0:P 1:L 2:A
        MOD = 10 ** 9 + 7
        dpPLA = [[1, 1, 1] for _ in range(n+1)]
        dpPL = [[1, 1] for _ in range(n+1)]
        dpPLA[0][1] = dpPLA[0][2] = 0
        dpPL[0][1] = 0
        
        for i in range(2, n+1):
            dpPLA[i][0] = (dpPLA[i-1][0] + dpPLA[i-1][1] + dpPLA[i-1][2]) % MOD
            dpPLA[i][1] = (dpPLA[i-1][0] + dpPLA[i-1][2] + dpPLA[i-2][0] + dpPLA[i-2][2]) % MOD
            dpPLA[i][2] = (dpPL[i-1][0] + dpPL[i-1][1]) % MOD
            dpPL[i][0] = (dpPL[i-1][0] + dpPL[i-1][1]) % MOD
            dpPL[i][1] = (dpPL[i-1][0] + dpPL[i-2][0]) % MOD
        # print(dpPLA)
        res = sum([dpPLA[n][k] for k in range(3)]) % MOD
        return res