'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''


def isHappy(n: int) -> bool:
    ns = str(n)
    sums = 0
    for n in ns:
        sums = sums + int(n)**2
    mark = set()
    while not sums in mark:

        if sums == 1:
            return True
        mark.add(sums)
        # print(sum)
        ns = str(sums)
        sums = 0
        for n in ns:
            sums = sums + int(n)**2
    return False