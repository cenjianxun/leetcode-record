'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.
'''

'''
1.重复的在字典里
2.首str为0的要去掉
3.搓 奇怪的解法
'''

class Solution:
    def comp(self, L):
        dic = {}
        long = ''
        short = ''.join([str(l) for l in L])
        for l in L:
            if len(str(l)) > len(long):
                long = str(l)
            if len(str(l)) <= len(short):
                short = str(l)
        longest = short + long
        for l in L:
            k = len(longest) - len(str(l))
            key = str(l) + longest[:k+1]
            if not key in dic:
                dic[key] = [l]
            else:
                dic[key].append(l)
        print(L, dic)
        temp = sorted(list(dic.keys()), reverse=True)
        result = [''.join([str(v) for v in dic[t]]) for t in temp]
        return result
            
            
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        dic = {}
        for n in nums:
            k = int(str(n)[0])
            if not k in dic:
                dic[k] = [n]
            else:
                dic[k].append(n)
        temp = sorted(list(dic.keys()), reverse=True)
        result = ''
        for k in temp:
            if len(dic[k]) == 1:
                result = result + str(dic[k][0])
            else:
                result = result + ''.join(self.comp(dic[k]))
        while len(result) > 1 and result[0] == '0':
            result = result[1:]
        return result

'''
就是自定义比较的样式，想那么复杂
两两比较的原始，字面意思就是比较 str(a) + str(b) 和str(b) + str(a)哪个大
就sort就行了。

1.顺一下各种排序。
2.sort 的py3 取消了cmp, 用key, 

def compare(x, y):
    return int(x+y) - int(y+x) 
要返回这个，而不能直接比较 return x+y > y+x 这个是错的。因为内建cmp函数，neg是小于，pos是大于
'''
def largestNumber(nums: List[int]) -> str:
    num = sorted(map(str,nums), key=cmp_to_key(lambda n1, n2: 1 if n1+n2>n2+n1 else -1), reverse = True)    
            print(num)
            return str(int(''.join(num)))  