'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

# faster than 20.60% of Python3
def isValid(s):
    char_dic = {'(':')', '[':']','{':'}'}
    if not s or len(s)%2:
        return False
    tempL = []
    slist = list(s)
    curp = ''
    while slist:
        curp = tempL.pop() if tempL else slist.pop(0)
        curq = slist.pop(0)
        if not char_dic.get(curp) or not char_dic[curp] == curq:
            tempL.extend([curp, curq])
  
    return False if tempL else True



s = "{[(])}"
result = isValid(s)
print(result)