'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
'''

'''
妙解法：看余数重复与否
'''

def fractionToDecimal(numerator: int, denominator: int) -> str:
    num = abs(numerator)
    den = abs(denominator)
    if numerator * denominator >=0:
        flag = ''
    else:
        flag = '-'
    
    s = num//den
    rest = num%den
    if not rest:
        result = str(s)
    else:
        result = str(s) + '.'
        hmap = set()
        while rest and not rest in hmap:
            hmap.add(rest)
            num = rest*10
            s = num//den
            rest = num%den
            result = result + str(s)
            # print(num, s, rest, result)

        if rest in hmap:
            r = rest
            num = rest * 10
            rep = str(num //den)
            rest = num%den
            while rest != r:
                num = rest * 10
                rep = rep + str(num //den)
                rest = num%den
            result = result.replace(rep,'') + '({})'.format(rep)
    return flag and flag + result or result 

'''
注意每一位对应的余数和商，何时该退出循环，退出的时候的状态
'''
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = '' if numerator * denominator >= 0 else '-'
        num, den = abs(numerator), abs(denominator)
        ans, rest = str(num//den), num%den
        if rest:
            num = rest * 10
            deci, deci_rest = [str(num//den)], [rest]
            rest = num%den
            print(num, den, rest)
            while rest and rest not in deci_rest:
                deci_rest.append(rest)
                num = rest * 10
                rest = num%den
                deci.append(str(num//den))
            print(rest, deci, deci_rest)
            if rest in deci_rest:
                index = deci_rest.index(rest)
                ans = ans + '.' + ''.join(deci[:index]) + '({})'.format(''.join(deci[index:]))
            
            else:
                ans = ans + '.' + ''.join(deci)
        return flag + ans

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = '' if numerator * denominator >= 0 else '-'
        num, den = abs(numerator), abs(denominator)
        ans, rest = str(num//den), num%den
        if rest:
            ans = ans + '.'
            deci_rest = set()
            while rest and rest not in deci_rest:
                deci_rest.add(rest)
                num = rest * 10
                rest = num%den
                ans = ans + str(num//den)
            if rest in deci_rest:
                start_rest = rest
                num = rest * 10
                rep, rest = str(num//den), num%den
                while rest != start_rest:
                    num = rest * 10
                    rep, rest = rep + str(num//den), num%den
                ans = ans.replace(rep, '({})'.format(rep))
        return flag + ans