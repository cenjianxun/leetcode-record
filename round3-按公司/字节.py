25* 39 79 91* 81 88 139 146* 213 127 207 224 286 239 300 301 347 399 295 300 617 652 694  698* 767 785 953 983 986 1428 993 1293 1366 1143 2096 1352

347 Top K Frequent Elements
235 Lowest Common Ancestor of a Binary Search Tree
236 Lowest Common Ancestor of a Binary Tree
146 LRU Cache
297 Serialize and Deserialize Binary Tree
45 JUMP GAME
55 JUMP GAME2
743 Network Delay Time BFS
286 Walls and Gates
300 Longest Increasing Subsequence
567 Permutation in String 2 Two pointer Sliding window
76 Minimum Window Substring Sliding window
253 Meeting Rooms II Two Pointer
496 Next Greater Element I
503 Next Greater Element II Stack
354 Russian Doll Envelopes
99 Recover Binary Search Tree
299 Bulls and Cows 2 Hash Table
341 Flatten Nested List Iterator Design
384 Shuffle an Array Array
398 Random Pick Index Hash Table
528 Random Pick with Weight Binary Search
295 Find Median from Data Stream
124 Binary Tree Maximum Path Sum
79 Word search
973 K Closest Points to Origin
25 Reverse Nodes in k-Group
790 Domino and Tromino Tiling DP
507 Perfect Number
780 Reaching Points
981 Time Based Key-Value Store
394 Decode String
49 Group Anagrams ‍‍‌‍‍
53 Maximum Subarray

get k most frequent numbers
follow up: what if the array is much larger than k
————————————————————
2022(4-6月) 码农类General 硕士 全职@字节跳动 - 猎头 - 技术电面 Onsite  | 😐 Neutral 😣 HardPass | 在职跳槽
TikTok 的面试方式比较特别，一轮一轮面，过了一轮才安排下一轮，战线拖的很长。前两轮都是 coding
第一轮 data 组面，简历延伸问了几个问题，我记得的有怎么保证 Kafka exactly once delivery，怎么 avoid shuffle when joining data in MR job，我自己感觉答得都不是太好。问完简历出了一道 SQL 题，我没有刷过 SQL 相关的题只能硬着头皮看，大概用到 count group by 和 case when，我直说记不住 case when 的 syntax，就换了一道 LC 19，写完大概讲一下就结束了。
一周之后第二轮，还是一个大组下的，自我介绍之后直接出的 LC 300，写完之后 follow up，如果返回的不是 max length 而是真正的 sequence 怎么做，直接‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌在 code 上改好之后 test 了几个 case 就过了。第二题没有在 LC 上找到，大概是给一堆 intervals，问最多可以找出几组 non-overlapping intervals of size 3，我也不太确定怎么做，最后我说的是拿 heap，写了一下伪代码草草结束了。


2022(4-6月) 码农类General 硕士 全职@字节跳动 - 网上海投 - 技术电面  | 🙁 Negative 😐 AverageFail | 在职跳槽
安排的周日晚上，是国内员工来面试，上来就说中文。自我介绍完毕后不问任何BQ，直接开始技术拷问。从数据库磁盘存储实现到网络通信协议全问一遍，普通码农要求这么高的吗？问了半小时开始出题，第一个是SQL查询，找出分数大于80的学生名字，很简单。第二个就是经典刷题网肆，二分查找嘛，我装作不会，一边‍‍‌‍‍解释思路一边敲代码。最后嫌我太慢超时了，但是也都给写完了啊。然后今天给我挂了，是嫌我假装不会吗？真不如上来直接暴力求解算了


2022(1-3月) 码农类General 硕士 全职@字节跳动bytedance - 内推 - 技术电面  | 😐 Neutral 😣 HardFail | 在职跳槽
申请的字节新加坡岗位，内推就没有做OA
1. 面试官在背景，问了一道数独的LC原题，问了问distributed lock 和项目相关
2. 面试官在新加坡，问了一道概率相关的LC原题，其它的印象不深了
3. 三面挂了，问了一道 complete tree，没有使用最优解，问了八股文 IPC
字节的推进速度很快，基本上上午面试完下午就会有结果，如果没有结果就是挂了，因为据说懒得给挂了的写feedback
楼主申请的‍‍‌‍‍是AI组的SDE，如果对大家有帮助可以帮我加米


2022(7-9月) 码农类General 硕士 全职@字节跳动 - Other - 技术电面  | 😐 Neutral 😐 AverageFail | 在职跳槽
我很久没有刷过新题了，所以大多都是临场发挥，两道题都做出来跑test cases通过了，后来还是挂了。
第一题： 2096. Step-By-Step Directions From a Binary Tree Node to Another
先做LCA，然后从lca用pre order分两次找到两个nodes的path，最后join两个path，coding的时候在push 和 pop中间结果的地方出了错被指出来改正了，最后能跑过。
time：O(N), space O(1)
我看网上很多解法是把tree转化成graph，然后做BSF，但发现time也是O（N）， space还是O（N）。不知道有啥更优化的方法？
第二题：1352. Product of the Last K Numbers
我最先说了native的解法，就算从list的最后计算k prodcut，直接不考虑。
然后我说明自己的优化，用一个hashmap记录前i个数的product，然后每一次add，计算当前所有number的product，然后再除前 n - k个数的prodcut（用到hashmap），这样time就下降到O（1），comment里面的test cases都能跑过。
corner case是有0的情况无法正确出结果，我想了‍‍‌‍‍半天，在面试小哥的提示下，想到用一个变量来判断最后k个数字是否包含0，如果不包含，则把0看作1，否者0还是0，这个地方想了很久，一直在埋头算，没有太多沟通，但是最后还是说出思路来了，我说要实现，因为还有8分钟，面试小哥说已经理解，不用了，然后我问了自己的问题就结束了。
现在我还是有点蒙，像这样的题，咋做才算pass？
——————————————————>>>>>>>>>>
第一题遍历了3遍，其实只需要DFS一遍找出root到两个点的路径即可，接下来就是对路径的处理。
可能是挂在第二题上了，肯定是用 preproduct，只是对0的处理不合人家心意吧。其实遇到0就把preproduct数组清空重置即可，而且也没必要用hashmap吧。输出结果时判定k大于preproduct数组长度的话就说明有0的存在。


2022(4-6月) 码农类General 硕士 全职@bytedance - 猎头 - Onsite  | 😃 Positive 🙂 EasyOther | 在职跳槽
新鲜的onsite，只有两轮，应该是过了才能有另外的两轮吧。 整体感觉HR和面试官态度都特别的好，不过我过不过就不知道了。。。。。
第一轮：
自我介绍，简单聊一聊，然后写了简单的题热一下身，给一个普通的二叉树，要求转换左右子树，问了一下树的高度如何，想用递归但是我怕爆栈，面试官说无所谓
然后是一个简单的dp，就是说a-z对应1-26，然后给你一串数字问转换成字母有多少种可能？比如“12”可以看成“1”和“2”也可以是“12”. 之后要求自己定义test case，然后跑一跑程序，测一下，问了复杂度，然后我说空间的可以滚动数组优化一下，然后优化的稀烂，，，，本来很简单的，但是有点紧张所有不知道为啥数组有的数据重合了，面试官说算了，也没深究，然后就问了问我有什么问题
第二轮：
自我介绍，随便聊了聊，然后给了一道题 输入是array of string，类似于 ["a", "ab", "abc", "bcdeff"]
目的是从空字符串开始找，每次只能加一个字符，然后看看随后找到的串是什么，这个例子里面是abc。 bcdeff很长，但是连最开始的"b"都没有所以根本搜不出来。
很直观，用trie就行了
面试官问道（或者是在提醒）问我每个节点是啥，是字符吗？我斩钉截铁的告诉他肯定不是字符，trie的每个节点是这个word，这个是principle。 处理掉几个typo，然后做了出来，然后面试官问让我列test case，问复杂度，跑一跑。都没啥问题，然后问我优化的事情，其实没想到啥，毕竟trie已经很快了。面试官说如果你要存字符的话，也许不一样，然后我就懂了，意思就是得sort一下input，这里我确实姜了：
第一：为了解决问题，trie存字符也没啥问题，没必要固执
第二：我想过剪枝，但是因为要sort就劝退了，但是问题是trie的复杂度是按照字符算的，sort的复杂度是按照word算的。on average，sort之后也许是要更快的，虽然也不一定。
总之我配合着面试官演完了整个optimization，虽然我觉得这个也没很优化毕竟worst case还是一样甚至更糟吧（如果有，请评论区指教一下，谢谢啦）。
然后就是喜闻乐见的反向interview，挺逗的，仿佛我是在考别人bq呢（你们work life balancing怎么样呀？那你遇到过什么什么情况吗？你们升职都是怎么弄的呀？等等），哈哈哈
整个流程我比较在意的就是第二轮面试官说我们没啥时间了，所以就不做第二题了，，，hmmm，这道题讨论了一段时间，尤其‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌是在纠结trie存什么的问题，所以真的写代码的时间也没有很长，半分钟解决typo，，，就算减少交流，很快完成，我觉得还是挺难做到第二题的，不知道大家啥情况。


2022(4-6月) 码农类General 硕士 全职@字节跳动 - 猎头 - 视频面试  | 😐 Neutral 😐 AveragePass | 在职跳槽
本帖最后由 匿名 于 2022-5-13 21:41 编辑
最近聊了一个字节的VO
1.自我介绍（需要突出自己的工作experience，技术栈，项目，中间件）
2.聊其中一个project：谈到redis的三种模式，redis热key的处理
3.后面延伸出kafka消息通道的信息，这里答的不太好，被问到了如何顺序执行‍‍‌‍‍


2022(4-6月) 码农类General 硕士 全职@bytedance - 猎头 - 技术电面  | 😐 Neutral 😐 AverageFail | 在职跳槽
题目是利抠81的变种，增加了两个限制要求，第一个是必须要在O(logn)完成，第二个是不知道原来array是ascending还是descending。


2022(4-6月) 码农类General 硕士 全职@字节跳动 - 猎头 - 技术电面  | 😐 Neutral 🙂 EasyFail | 在职跳槽
常年不发帖，但这次真不得不吐槽了。国人面试官，题目都不难，救物叁和简化的亿思耳爸（面的题直接给了matrix，所以就是一个纯search的题）。聊的过程中，其实也挺好，不过万万没想到竟然把我挂了，从hr得到的反馈说，“overall well”，但说我交流上有问题，面试官希望我写代码前，先说清楚思路再写code。拜托，我面试的开头就问面试官，“因为时间有限，而且需要跑test，我能不能先写一些必要的template code，顺带思考下一些实现的细节”，他说了可以，我才继续先写code，写完之后我把整个流程解释清楚，他也表示完全理解。
除非要么是大佬，要么是背题家，我这种没见过这题，只能循序渐进写一个非最优解的很显然配不上tiktok。第二题的解法，我的做法(O(mlogn))确实不是最优解(O(m+n)，如果真用这个理由挂我，我会觉得不爽，但能理解；但用交流能力挂我，我真心不服，因为这是最开始面试前两边都同意的。何况他‍‍‌‍‍还不是我申请的组，凭什么用这种理由挂我？我自己当面试官的时候从来都是让candidate自己选，因为有些candidate进入状态慢（比如我这种菜狗），需要先敲代码找一下感觉，捋一下思路，但只要最后能得听到他的解题思路，并能成功跑一些test case就行。大家凭良心说，这种能不能当reject的理由吧。


2022(1-3月) 码农类General 本科 全职@bytedance - 网上海投 - 技术电面  | 😐 Neutral 😐 AverageFail | 应届毕业生
一月份左右面的字节SRE，店面
面试官是个中国人，开场打了个招呼后面就都用中文交流了
问了操作系统，计算机网络，数据结构，等等。
操作系统的话就是进程与线程和其他一些不太记得了
网络就是tcp，ip。 其中有问三次握手如果只做两次会怎么样， 还有tcp和udp的区别，应用场景
数据结构印象还蛮深的，问了一个有一亿个url怎么去重。 我回答的是hashmap，但明显不是他想要的答案 （楼主也不知道正确答案是啥），后来就沿着hashmap问下去了。
比如hashmap是怎么实现的，以及hashmap的key会有重复的吗等等
不难但是很杂， 涉及面很广
最后做了一道题，一个linked list有loop， 找到loop的入口。 很经典的题目，但是当时我忘了怎么用two pointe‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌r做了最后直接用了hash map 当作答案。。
求大米呀！


2022(1-3月) 工程类 硕士 全职@字节跳动 - 猎头 - Onsite  | 😐 Neutral 😐 AveragePass | 在职跳槽
本帖最后由 匿名 于 2022-3-30 17:10 编辑
去年年底 ByteDance 来联系说要给面试，就面了一下。三轮都很顺利，最后和 HR 聊完决定不去。前来分享一下面试题。
求各位看官加点大米。好久不用这个账号现在已经没有大米了。给帖子加大米不会影响你自己的大米数量哦。
第一面
第一面题目是给一个 0-1 矩阵，问里面有多少种形状。里面的横向或纵向连接的 1 可以组成一个形状，两个仅有位移差别的形状算作同一种形状。
给四十五分钟到一小时，实现是用 backtracking，时间复杂度应该是 O(mn) 如果用 m 和 n 表示矩阵的长宽。
第二面
第二面题目是写一个玩五子棋的平台。题目就这么多，具体怎么做都看你自由发挥。
我的做法是用 Python 写了一个命令行程序，不断轮流让玩家（黑子或者白子）输入‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌要落子的坐标，然后如果游戏结束就打印出胜方。面完我觉得面试官很满意。
第三面
第三面是 behavioral，聊了一些有的没的。问题不太记得了但没什么异乎常规的。
求加大米 :Orz


2022(1-3月) 码农类General 硕士 全职@字节跳动 - 猎头 - 视频面试  | 🙁 Negative 😐 AverageFail | 在职跳槽
Linkedin上被tiktok的hr联系，马上约了hr talk和面试。tiktok的面试一共是三轮，每一轮过了才会有下一轮，没想到第一轮就跪了。。
之前看了地里所有的tiktok面经，做了不少算法题，信心满满的去面试。
以下内容需要积分高于 100 您已经可以浏览
面试的是一个年轻的中国面试官
上来一套八股文把我问懵了，问了算是在国内面试的几个经典考题
1. 一个数组表示的无序数组如何建立最小堆的过程
2. 数据库的隔离模式
3. java volatile vs synchronized
还有一些小问题忘记了，基本上就是问实现原理。我对此完全没有准备，只能凭感觉说个大概，感觉问完面试官已经就想结束了。
最后coding考了两道题
https://leetcode.com/problems/reverse-nodes-in-k-group/
和一道非常简单的binary search题， 20分钟秒了两道题，面试官问有没有什么问题就草草结束了。
整个面试过程没有问任何简历相关的问题，包括之前做的项目的细节。
一部分是自己太菜了，一部分是自己完全‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌没有准备这些问题。 面试官态度不冷不热，不过明显感觉在问完八股文之后面试官就不太想进行下去了，后面也就是走流程。感觉是挺差的一次面试体验。
希望给后面面试的同学提供一些经验，要是hr找你要china-based time zone，是中国面试官的话，一定要好好准备基础知识。


2022(1-3月) 码农类General 硕士 全职@字节跳动 - 网上海投 - Onsite  | 🙁 Negative 😐 AverageFail | 在职跳槽
面的2-2，ads组
第一轮题不大记得了，但非常肯定是地里的面经题，而且不难
第二轮直接就上system design了，设计一下抖音的评论系统，从API到data schema再到architecture
第三轮我本来以为就是hm轮了，来的人一看也的确是hm，结果先迟到五分钟不说，一开始跟我讲先问问简历讲讲project，再留30分钟左右做个design，结果聊完project，又突然说咱们做道题再design吧，行，做了个spiral matrix。咱们再做一题吧，靠，岛屿数量，做完了，又来了个followup，问假设matrix里面就一个岛（没有内陆湖），并且给你岛上随机的一个点，怎么找岛屿的上下左右边界。我写了个N^2的BFS，没让我写完，最后在提示下写了个大概Nlog‍‍‌‍‍‌‌‌‌‌‌‍‍‍‍‌‌‍‍‌N的binary search
实在是无语，大哥你面试流程这么随意的嘛，中间接电话还让我干等五分钟。
三天后收到拒信


新加坡的印度大姐先是花了20多分钟聊了简历，问了一些DDIA里面的知识点，类似于解释btree lsm的index怎么实现的，以及cold storage底层怎么实现？然后甩了一道看起来简单，但最优解不好想的题…我给了一个次优解，大姐死活不让我写，让我在那干想了15分钟。最后估计可怜我让我写了次优解，bug free5分钟写完了，依旧转手挂了我。
题就是给你一个2d matrix，只有0和1，每个row自己都是sorted，row和r‍‍‌‍‍ow之间没啥关系。求左边起第一个遇到的1的坐标。
00111
01111
0001
0000
输出1，1 因为第二行的1在最左边