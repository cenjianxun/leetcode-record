# 看123 218 341

看天际线 线段树 环状数组

子串：连续的一部分 substring
子序列：不连续但是先后顺序相同 subsequence
# ============================
二位数组dfs不知何时返回，遍历完返不返回不确定：
79

# ============================


# # —————————— 位运算 | 布尔运算 ———————————
# 位运算
^ 异或：a ^ b  
① 两值相同为0 
② 与0异或值为它本身

# 骚操作 191. Number of 1 Bits
1. << 等于 *2; >> 等于 /2
2. n&(n-1) 意思是：n的最后一位1变成0，这1之后的0都变成1
	可用这种方式数n里有多少个1，重复几次n&(n-1)直到n==0时，就有几个1
3. ~0==-1，~-1==-2，~-2==-3 ……

# 布尔运算
1. 差集：set1 - set2
2. 对称差集: set1 ^ set2 # 取集合 A 和 B 中不属于 A&B 的元素
	if a ^ b = c, 则 c ^ b = a, c ^ a = b

#进制转换 190. Reverse Bits
1. x进制转10进制：int(str(n), x) 
① 本身要是str
② 第二个参数是本身进制而不是10进制
2. 10进制转2进制：bin(n) 
①前面会有一个b，需要 s = str(bin(n))[2:]
②不一定是32位看下题目。补充位数：前面加0：'0'*(32-len(s)) + s

# 加法
a和b为int
进位表示为：carry = (a & b) << 1 # 往左进一位
本位留值为：x = a ^ b
下一轮的ab为carry和x
'''
int getsum(int a, int b){
	if (a == 0){
		return b;
	}
	while (a != 0){
		int carry = (a & b) << 1;
		b = a ^ b;
		a = carry;
	}
	return b;
}
'''
# —————————— string ———————————
# 计字符串元素及个数
from collections import Counter
sMap = Counter(aString)

# string的函数
.lower() 小写 # 返回小写，原str不变
.isalnum() 是否字母数字
.isalpha()

# 字母和数字转化
i = ord(char) - ord('a')
char = chr(i + ord('a'))
# —————————— set ———————————
# 增删
set1.add(a) O(1)
set1.remove(a) O(1) # 没有a会报错
set1.discard(a) O(1) # 没有a不会报错
set1.pop() # 随机删除一个


# —————————— list ———————————
# 增删
alist.append() O(1)
alist.insert(index, value) O(n)
alist.pop(index) O(n)
alist.remove(value) O(n)

#list的index：
alist.index(astr) 返回alsit里【第一个】astr的序列号


# 队列
from collections import deque
q = deque(alist) #赋值
deque.popleft()
deque.appendleft()

# 堆
import heapq # 它是小顶堆/最小堆 min_heap,也就是堆顶元素始终是堆中最小的元素
1. 创建：
	heap = []
	for n in data:
	    heapq.heappush(heap, n) # heap要提前创建个list
	或者：
	heapq.heapify(data) # data本身就变成堆

2. 弹出：
	heapq.heapify(data)
	for i in range(2):
		smallest = heapq.heappop(data)

3. 删除并替换成新值
	heapq.heapify(data)
	for n in [0, 13]:
	    smallest = heapq.heapreplace(data, n)

	# 在一个操作中将num添加到堆并从heap中删除最小项
	heapq.heappushpop(heap, num)

4. 找范围
	heapq.nlargest(3, data) # 最大的前3个 按从大到小
	heapq.nsmallest(3, data) # 最小的前3个 按从小到大

5. 找第k
	找第k大的元素，用小顶堆。因为当 len(list)>=k时，再进去值时，被替换出来的是堆顶=【最小的值】。
	所以当循环完了之后，里面剩的是最大的k个值，且第k个是堆里最小的。

	找第k小的元素，用大顶堆。pushpop出的是堆定=最大的值。完之后剩的是最小的k个值

	模板：
		if len(heap) < k:
			heapq.heappush(heap, x)
		else:
			heapq.heappushpop(heap, x)

		return heap[0]

# —————————— dict ———————————
# defaultdict
from collections import defaultdict
普通的dict如果没有，会报错
dic = defaultdict(value的类型)，如果没有默认为空
🟡 如果要指定初始值，比如正无穷，可以用匿名函数:
	defaultdict(lambda:float('inf'))

#删除：
value = dic.pop(k)
subdic = dic.popitem(k)
del dic[k]
del dic
dic.clear()


# —————————— tree ———————————
# 树的序是针对根说的：
前序：根左右。 preorder
中序：左中右。 inorder
后续：左右中。 postorder

# 二叉搜索树：
左边 < 中间 < 右边


# —————————— 其它 ———————————
# enumerate
enumerate(s, i) 意思是从索引i开始
index, value in enumerate(s, i) 只有index从i开始！！value还是从第一个开始

# 构建双重数组容易记混：
[[0] * len(l2) for _ in range(len(l1))]
[[0 for _ in range(len(l2))] for _ range(len1)]
点在于：
如果 * 个数，[]的"]"就要单独
如果 for 循环个数，[] 就要把for循环放进[]

# bisect
alist # 是一个【升序】list
i = bisect.bisect_left(alist, num)
↑ 如果把num插入alist的话且num左边的值都<num的话，插入的是第i个
i = bisect.bisect_right(alist, num)
↑ 如果把num插入alist的话且num左边的值都<=num的话，插入的是第i个
bisect.bisect() = bisect.bisect_right()

❗❗ 此时并没有插入！
要插入还是要alist.insert(i, n)
=> insort(seq, item, lo, hi) 把变量 item 插入到序列 seq 中，并保持 seq 升序
	bisect.insort(alist, num) 直接插入了
❗❗ 这个i是假设插入了以后，这个被插入值的index

& insort(index, num)
& heappush(alist, num)


# 幂和开方
pow(n,x) #n的x次方
math.log(n, 3) #n开3次log


# random
从alist里随机选一个：random.choice(alist)
让alist乱序排列：random.shuffle(alist)
[0,1]里选实数：random.random()
[i,j]里选整数：random.randint(i,j)
[x,y]里选浮点数：random.uniform(x,y)
[i:j:n]里选间隔n的整数：random.randrange(i,j,n)


# cmp 
cmp(x, y) 
x < y 返回 -1; x == y 返回 0; x > y 返回 1


# —————————— 时间为N的排序算法 ———————————

计数排序 | 基数排序 | 桶排序

🟡计数排序：

对每个元素值统计频次. 然后从小到大扫描, 将每个元素值重复若干次.

缺点：
如果元素值范围非常大, 那么几乎不会出现重复的元素, 造成效率低下。也开不了这么大（10^16）的数组用于计数
如果元素值是浮点数的话, 也几乎不会出现两个相等的元素.

总结：计数排序适用于小范围的整数型元素的数组排序.


🟡基数排序：

按照每一位的位数排序，放入10个桶里。位越高, 对数字大小的影响越大, 因此, 算法的顺序必须是从低位到高位。

比如： [88, 16, 34, 16, 63, 1, 4, 99, 31, 80, 56, 53, 68, 79, 89, 18, 84, 29, 46, 8]
先按个位数排序：[80, 1, 31, 63, 53, 34, 4, 84, 16, 16, 56, 46, 88, 68, 18, 8, 99, 79, 89, 29]
再按十位数排序：[1, 4, 8, 16, 16, 18, 29, 31, 34, 46, 53, 56, 63, 68, 79, 80, 84, 88, 89, 99]

严格说来, 基数排序的时间复杂度为O（k*n）, k为最大数的位数。
但是, 一般说来, k不会太大, k = 30的话, 已经是天文数字了, 因此, 基数排序的时间复杂度可以算做O（n）, k就当成常数项即可。

总结：基数排序适用于整数型元素, 不怕数值范围太大, 这点要比计数排序强。


🟡桶排序：
 
每个桶的宽度 width = max(1, (数组最大值 - 数组最小值) // (数组长度 - 1))
桶的个数 N = (数组最大值 - 数组最小值) // width + 1
每个数的位置（哪个桶）location = (nums[i] - 数组最小值) // width
* 桶是左闭右开