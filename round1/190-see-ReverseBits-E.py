'''
Reverse bits of a given 32 bits unsigned integer.
'''
'''
1. x进制转10进制：int(str(n), x) ① 本身要是str， ② 第二个参数是本身进制而不是10进制
2. 10进制转2进制：bin(n) ①前面会有一个b，②不一定是32位看下题目
'''

def reverseBits(n: int) -> int:
    print(bin(n))
    n = str(bin(n)).split('b')[1]
    n = '0' * (32 - len(n)) + n
    print(n)
    return int(''.join(list(n)[::-1]),2)