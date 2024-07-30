'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

'''
需要除掉空格，还要把数字放一起
太慢了看看其他解法
'''

def calculate(s: str) -> int:
    slist = [s for s in list(s) if s.strip()]
    stack = []
    while slist:
        n = slist.pop()
        if not n in '+-*/' and stack and not stack[-1] in '+-*/':
            n = n + stack.pop() 
        stack.append(n)
    # print(slist)
    # print(stack)
    while stack:
        n = stack.pop()
        if n in '*/':
            o = n
            n = int(slist.pop())
            d = int(stack.pop())
            if o == '*':
                n = str(n * d)
            if o == '/':
                n = str(int(n/d))
        slist.append(n)

    # print(stack)
    slist = slist[::-1]
    while slist:
        n = slist.pop()
        if n in '+-':
            o = n
            n = int(stack.pop())
            d = int(slist.pop())
            if o == '+':
                n = str(n + d)
            if o == '-':
                n = str(n - d)
        
        stack.append(n)
    # print(stack)
    return int(stack[0])
                    

'''
循环。因为做运算涉及运算符两边的数字，进栈的是前一个。
所以首先需要进栈。
所以如果遇到有运算符，前一个数进栈。
然后因为延迟了，所以运算符需要临时变量记录，当辨识到下一个运算符的时候，本轮的后位数字得到，才参与运算。
所以是延迟循环一轮的
所以给原本的字符串加一个 '+0'
'''
def calculate(self, s: str) -> int:
    res = []
    num = 0
    sign = '+'
    for e in s+'+0':
        if e.isdigit():
            num = num * 10 + int(e)
        elif e in '+-*/':     
            if sign == '-':
                num = -num
            if sign == '*':
                num = num * res.pop()
            if sign == '/':
                if res[-1] < 0:
                    n = res.pop()
                    num = -(-n//num)
                else:
                    num = res.pop()//num
                print(num)
            res.append(num)
            sign, num = e, 0
    return sum(res)

'''
顺便说👆巧妙的地方是res里面是最后都要加的数，要减的直接变负数

自己做有很多要注意的地方：
1. str里有空格
2. str的字符是数字，不仅仅是单个！！！，要把数字连起来
3. 如果实在没把握就左入右出，否则会把被减数和减数搞混
'''