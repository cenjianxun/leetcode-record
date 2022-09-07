''''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 
'''

'''
faster than 11.17% of Python3
'''

def eachRow( pre_l):
    if not pre_l:
        return [1]
    l = []
    temp_l = [0]
    temp_l.extend(pre_l)
    temp_l.append(0)
    print(temp_l)
    for i in range(1, len(temp_l)):
        l.append(temp_l[i-1]+temp_l[i])
    return l
    
def generate(self, numRows: int) -> List[List[int]]:
    result = [[]]
    while numRows:
        row = eachRow(result[-1])
        result.append(row)
        numRows = numRows - 1
    return result[1:]