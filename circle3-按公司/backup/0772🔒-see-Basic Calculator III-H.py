'''
772. Basic Calculator III [🔒]

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

	"1 + 1" = 2
	" 6-4 / 2 " = 4
	"2*(5+5*2)/3+(6/2+8)" = 21
	"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

Note: Do not use the eval built-in library function.
'''

'''
要注意的就是 '-5'.isdigit() 是False，这个函数只能查str的正数
'''
def calculate(s: str) -> int:
	stack = []	
	print(s)
	for e in s:
		if e.isdigit():
			if stack and stack[-1].isdigit():
				e = stack.pop() + e
			stack.append(e)
		elif e in '+-*/()':
			stack.append(e)
	print(stack)

	def cal(expression):
		#print(expression)
		res = []
		i, op = 0, ''
		for i, e in enumerate(expression):
			if e.isdigit() or e[0] == '-' and e[1:].isdigit():
				if op in '+-':
					#op = op.replace('+','')
					res.append(int(op+e))
				elif op == '*':
					res[-1] = res[-1] * int(e)
				elif op == '/':
					res[-1] = res[-1] // int(e)
			elif e in '+-*/':
				op = e
		#print(res)
		return str(sum(res))


	while stack.count('('):
		right = i = stack.index(')')
		while stack[i] != '(':
			i -= 1
		stack = stack[:i] + [cal(stack[i+1:right])] + stack[right+1:]
		#print(stack)

	return int(cal(stack)) 

s = ["1 + 1", " 6-4 / 2 ", "2*(5+5*2)/3+(6/2+8)", "(2+6* 3+5- (3*14/7+2)*5)+3"]
ans = [2, 4, 21, -12]

i = 3
res = calculate(s[i])
print(res == ans[i] and True or False)
print('output', res)
print('ans', ans[i])