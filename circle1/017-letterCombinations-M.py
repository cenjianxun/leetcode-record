'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
'''

def letterCombinations(digits):
    # 可以用list，index相当于key
    d_to_l = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = []
    if not digits:
        return result
    def oneComb(l, d):
        # print(l)
        tempL = []
        for i in l:
            print(i)
            tempL.extend([i+s for s in d_to_l[d]])
        return tempL
    
    result = list(d_to_l[digits[0]])
    if len(digits) == 1:
        return result
    for i in range(1, len(digits)):
        result = oneComb(result, digits[i])
    return result

r = letterCombinations('234')
print(r)