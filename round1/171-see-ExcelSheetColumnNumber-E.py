'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
'''

'''
细节。最后一位单独
'''

def titleToNumber(columnTitle: str) -> int:
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    ln = len(columnTitle)
    result = 0
    for i in range(1, ln):
        result = result + 26 ** i
    col = list(columnTitle)
    while len(col) > 1:
        s = col.pop(0)
        result = result + 26**len(col)*(dic[s]-1)
    result = result + dic[col[0]]
    return result

'''
是26进制转10进制！！
'''
def titleToNumber(columnTitle: str) -> int:
    res = 0
    for c in columnTitle:
        res = res * 26 + ord(c) - 64
    return res