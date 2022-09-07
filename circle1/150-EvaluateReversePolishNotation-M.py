'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''

'''
注意只有一个的情况
不用eval，就分四种情况
'''

'''
python是向下取整
c语言是向0取整
这道题是向0取整
'''

def evalRPN(tokens: List[str]) -> int:
    stack = []
    tokens = tokens[::-1]
    operator = '+-*/'
    s = ''
    while tokens:
        cur = tokens.pop()
        while tokens and not cur in operator:
            stack.append(cur)
            cur = tokens.pop()
        if not cur in operator:
            result = int(cur)
        else:
            b = stack.pop()
            a = stack.pop()
            # print(a,b,''.join([a,cur,b]))
            result = int(eval(''.join([a,cur,b])))
        stack.append(str(result))
    result = int(stack[0])
    return result