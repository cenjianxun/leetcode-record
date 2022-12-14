———————————————— NO.1 动态规划 ———————————————— 
一般用于求最值

核心问题是穷举
→ 因为穷举会出现重叠子问题 
→ 使用备忘录或dp table来优化穷举过程

动态规划一定具备最优子结构
→ 子结构相互独立

列出正确的状态转移方程：
【明确[状态] → 定义dp数组/函数的含义 → 明确[选择] → 明确base case】
状态：原问题和子问题中变化的变量
dp函数的定义
选择：对每个状态，可以做出什么选择改变当前状态

没有分叉，一路推理 ➜ 〔线性结构〕
看到决策结果有分叉 ➜ 〔树形结构〕
若在推理过程中，产生交汇 ➜ 〔图结构〕


字符串匹配问题：44



💥硬币问题：

💥回文子串：5 647 300 718 1143 1035 53 392 115 583 72 674 516
https://leetcode.cn/problems/longest-palindromic-substring/solution/dai-ma-sui-xiang-lu-5-zui-chang-hui-wen-kgyl1/

	🔸5 vs 647🔸

	647 是求回子个数，5 是求最长回子。
	所以647不允许重复，一定要严格按着当前i为中心点往两边扩散，再分奇偶讨论。
	5算重了就重了，反正是求最大。
	除了可以中心扩散，还可以用dp。dp[i][j]就表示从i到j。注意需要从左下转移至右上，因为dp[i][j]的值需要由dp[i+1][j-1]来求得。


	🔸718 vs 1143 vs 1035🔸

	718是求最长子串，1143是求最长子序列。1035和1143一模一样。 
	都要按顺序，但子串subarray不能跳，子序列subsequence可以跳。
	子串转移方程是 dp[i][j] = dp[i-1][j-1] + int(A[i]==B[j])，dp[i][j]表示0..i 0..j间的公共子串长度
	子序列转移方程需要分A[i] 是否等于B[j]，
	如果相等，dp[i-1][j-1] 直接+1；
	如果不等，选dp[i-1][j]和dp[i][j-1]较大的。
	反例就是 'bsb' 'kbkb'，当两个str的第一个b已经相互匹配过，下一次就不能再重复用，所以一定是dp[i-1][j-1]基础上看i和j，此时确定i和j匹配，卡住，然后只看前面。 
		但是因为可以跳str，所以如果不等的时候，0i和0j匹配实际上可能是0i和0j-1匹配，也可能是0i-1和0j匹配。所以要选最大的。

	🔸583 vs 72🔸

	583是删除一个字母匹配，72是可删除、添加、替换 来匹配
	如果不需要删除，dp[i][j] = dp[i-1][j-1]
	如果需要删除 删除个数是 dp[i][j] = dp[i][j-1] + 1 # （第j个删除）
								   = dp[i-1][j] + 1 # （第i个删除）
	从i->j, 添加: dp[i-1][j] + 1
			删除：dp[i][j-1] + 1
			替换：dp[i-1][j-1] + (如果不同就替换，相同就不用替换)


💥抢劫问题

	🔸198 vs 213 vs 337🔸
	共同：如果祖rob，子不能rob，孙提供最大值
		 如果祖不rob，子提供最大值
	环状：去头答案 并 去尾答案 选优
	树状：可以返回一对值，{选它的值，不选它的值}
		return (cur.val + left[1] + right[1], max(left) + max(right))

	🔸91 vs 639 🔸
		种类计算是
		dp[i] = dp[i-1] + dp[i-2]
		639 多了不确定的*，那么本位从1种情况变成了x种情况，
		所以完整的转移方程其实是：
		dp[i] = dp[i-2] * (s[i-1:i+1]的种类) + dp[i-1] * (s[i]的种类)


💥 背包用动归
	【用dfs（没带cache）会超时】
	背包：容纳带价值和个数（重量）的物品，一般限制个数（重量），以达到价值最大。
		完全背包：每件物品可取无数次。
		0-1背包：每件物品最多取一次。

	01背包：
		dp[i][j] 表示前i件物品放入容量（用来限制个数/重量的度量单位）为j的背包的最大价值。
		转移过程有两种：选第i件（可放可不放） & （只能）不选第i件
		- 选第i件： dp[i][j]=max{ dp[i−1][j], dp[i−1][j−wi]+vi}
					wi是第i件物品的个数/重量，vi为第i件物品的价值。
					需要满足wi ≤ j
		- 不选第i件：dp[i][j]=dp[i−1][j]

		求问也有两种：恰好装满 & 不超过。 
			其中一个区别在于初始化，即啥都没放时候的合法状态。
			- 恰好装满：dp[i][0] = 0, dp[i][1,2,……,n] = −∞
				因为此时只有容量为 00 的背包可能被价值为 00 的 nothing “恰好装满”，
				而其它容量的背包均没有合法的解，属于未定义的状态。
			- 不超过背包容量：dp[∗][∗] 都 = 0
				因为对应于任何一个背包，都有一个合法解为 “什么都不装”，价值为 0。

	完全背包：639 322
		方案已并非取（取1件）或不取（取0件）两种情况，而是有取0件、取1件、取2件...取k件等很多种。
		- 第i件物品选0个的最大价值 dp[i-1][j]；
		- 第i件物品选1个的最大价值 dp[i-1][j-wi] + vi
		- 第i件物品选2个的最大价值 dp[i-1][j-2⋅wi] + 2⋅vi
			......
		- 第i件物品选k个的最大价值 dp[i-1][j-k⋅wi] + k⋅vi
 		*  第 ii 件物品能放入 kk 件的前提为：k⋅wi≤j
 		转移方程：
 			dp[i][j]=max{ dp[i−1][j−k⋅wi]+k⋅vi}, 0<=k⋅wi<=j
 		=>  dp[i][j]=max{ dp[i−1][j],dp[i][j−wi]+vi},0<=wi<=j
 		初始同01背包

 	对比：
 		01：  dp[i][j]=max{ dp[i−1][j], dp[i−1][j−wi]+vi}
 		完全：dp[i][j]=max{ dp[i−1][j],dp[i][j−wi]+vi}

	🔸474 vs 279🔸
		474:01背包
			有两个物品需要放入，因此有三层，j层表0，k层表1。
			❣❣❣ dp是把每个状态都列出来当step，而不是把每次添加当一次step
			所以dp j层和k层的长度是题中每个物品的上限。

			压缩：i层可以去掉，因为i只取决于i-1。要倒序。
		279： 完全背包




动归：5 516 139 517 53 91 639 650 {651} 198 213 337 174 15 674 377 322 518 221 673 764 416 494 309 714 678 10 44 689 {265} {276} 368 790 474 808 375 813 {294} {562} {361} 552 {568} 72 583 486 312 {727} {471} 403  1143 279

1400 不递归吧？注意点是要 len(s) >= k

没做：517 808 375 790(可以做) 等会做[10 44]
好题 474 813 312 368
———————————————— NO.2 贪心 ————————————————


💥股票问题：
https://leetcode.cn/circle/article/qiAgHn/
121, 122, 123, 188, 309, 714


没做 135 44 649
贪心：
406 45 135 316 621 122 55 455 392 134 714 452 330 738 659 376 502 {253} {759} 435 {651} {484} {358} 1053
————
738 452 605 621 253 484 316 {418} {774} 358 55 135

好题：45 316 加油站134

————————————————————————————————

Unique Paths	★★	
** 62	63	64	120	
*** 174	931 1210				

Maximal Rectangle	★★★	
85
* 304		
** 221	1277

House Robber	★★★	
** 198	213	309	740	790	801

Longest Subsequence	★★★	
300	5 32 516 647 718 1143
** 673	1048

Word Break	★★★	
139	
*** 140	818

Coin Change	★★★	
** 322	377	416	494	1043 1220 /1230/ 1262 1269

Edit Distance	★★★	
** 72	583 712	1143 718
*** 10	44	97	115	1092 1187 

Largest Sum of Averages	★★★★	
813	 
*** 1278 1335	410	

Dice Roll Simulation ★★★★
1223

Burst Balloons	★★★★
** 312	 1024	1039	1140	1130
*** 664	

Find the Shortest Superstring	★★★★★	
*** 943	980	996	1125




