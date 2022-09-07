'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''
'''
1.numpy可以自动32位。用np.int32()
2.最后需要用int()转化
3.位移运算符优先级大于或且非 https://www.cnblogs.com/uncle-jay/p/7823209.html
'''
import numpy as np
# faster than 5% of Python3
def getSum(a: int, b: int) -> int:
    while b:
        a, b = np.int32(a^b), np.int32((a&b)<<1)
    return int(a)


'''
导入numpy会变慢很多
'''
# https://darktiantian.github.io/371-Sum-of-Two-Integers-Python/
# https://www.hrwhisper.me/leetcode-sum-two-integers/

'''
计算加法：
不是一位一位的相加，而是一起相加，所以a+b == a^b + a&b<<1，那么下一轮的a和b就可以是本位a^b和进位a&b<<1。因为是同时计算的，那么跳出循环停止的条件就是进位为0。

位运算：
1. 二进制负数在底层或参加运算时的存储形式是补码，最高正负号位不变仍为1，其他位取反，再+1
2. python说不限制意思是它仅依靠正负号判断正负，而不用二进制最高位是否唯一，所以一个1111，在别的语言里就是-7，在python里就是15。会造成矛盾
3. 一般默认是32位的。32位就是0xffffffff
4. 问如果算出来某一次高于32位的怎么办？就不要了！直接不用算，所以在中途&ffffffff
5. 节点是7fffffff，所以有一些算法 最终判断是
	return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
	为什么节点是这个呢，因为这个值之下的数最高位都为0，反之为1。见2，本来大家默认最高位如果是1的话是负数，但是在python里最高位是1的话就仍然是正的该值。 此处a的字面值是负的情况下，表现出来为该负值的补码，就是一个>7fffffff的数，但它应该是负数，如果被python解释器算出来就是大正数，所以应该修正为由这个补码对应的真值。
	a>>31，表示把a的最高位32位，调到个位，再&1，同样也可以判断最高位是不是1
6. ~0==-1，~-1==-2，~-2==-3。。。
7. ~0<<31，就是把-1移到（右边）第32位（同时是负的）
8. a|(~0<<31)，是将32位及再往右的所有位都置1，在python里，负数怎么判断表示，补充②，是想象所有右边位都是1，在第二条里，1111之所以是15是因为它是0000…00001111，如果是负数的话应该是1111……00001111。那么本题32位，应该是32位及所有右边都为1，那么可以用(~0<<31)来|a
'''

# faster than 79.64% of Python3
def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    while b:       
        a, b = (a ^ b)&mask , ((a & b) << 1)&mask
    if (a>>31)&1:
        return a|(~0<<31)
    return  a


def getSum(a: int, b: int) -> int:
    # 32 bit mask in hexadecimal
    mask = 0xffffffff
    # works both as while loop and single value check 
    while (b & mask) > 0:
        a, b = (a ^ b), ( a & b ) << 1
    # handles overflow
    return (a & mask) if b > 0 else a
