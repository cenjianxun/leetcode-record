'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

可以用*号！！
'''

'''
自己base翻倍和多乘一次不是一件事
'''

def myPow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    
    flag = 1
    if n < 0:
        flag = -1
        n = -n
    result = 1
    base = x
    while n > 1:
        if n%2:
            result = result * base
            n = n - 1
        else:
            base = base * base
            n = n >> 1
    result = result * base
    if flag < 0:
        return 1/result
    else:
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        return result

'''
坑点：
while内的位置顺序 return 的判定放最上面
乘法初始值就是1 加法初始值是0

* 上面方法好。 n倒着来
'''
def myPow(self, x: float, n: int) -> float:
    if n == 0:
        return 1
    flag = 1 if n > 0 else 0
    n = abs(n)
    i = 1
    res = x
    rest = 1
    rest_i = 0
    
    while rest_i + i <= n:
        if rest_i + i == n:
            return rest * res if flag else 1/(rest * res)
        pre = res
        i = i * 2
        res = res * res
        if rest_i + i > n:
            rest_i = rest_i + i/2
            rest = rest * pre
            res = x
            i = 1