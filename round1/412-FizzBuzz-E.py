'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
'''

# >=61%
def fizzBuzz(n: int) -> List[str]:
    result = []
    for i in range(1, n+1):
        if not i%3 and not i%5:
            result.append('FizzBuzz')
        elif not i%3:
            result.append('Fizz')
        elif not i%5:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result