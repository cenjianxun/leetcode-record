'''
Minimum Swaps To Make A Binary String Palindrome

Give a binary string consisting of 0’s and 1’s only. E.g., 0100101. We are allowed to pick
any two indexes and swap them. We have to return the minimum number of swaps required to make
it a palindrome or -1 if it cannot. The string 0100101 can be made a palindrome by swapping
(3,4)-> 0101001 and swapping (0,1) -> 1001001 which is a palindrome. In this case, the
correct answer is 2.
'''

def check_length(n):
    # Length
    ans = 0
     
    while (n):
        # Right shift of n
        n = n >> 1
        # Increment the length
        ans += 1
    # Return the length
    return ans
 
# Function to check if the bit present
# at i-th position is a set bit or not
def check_ith_bit(n, i):
    # Returns true if the bit is set
    if (n & (1 << (i - 1))):
        return True
    else:
        return False
 
# Function to count the minimum
# number of bit flips required
def no_of_flips(n):
    # Length of the binary form
    ln = check_length(n)
 
    # Number of flips
    ans = 0
 
    left, right = 1, ln
 
    while (right < left):
 
        # Check if the bits are equal
        if (check_ith_bit(n, right) !=
            check_ith_bit(n, left)):
            ans += 1
 
        # Decrementing the
        # left pointer
        left -= 1
        right += 1
 
    # Returns the number of
    # bits to flip.
    print(ans)
    return ans
 
# Driver Code
n = 12
print(int('1010100', 2))
no_of_flips(84)
 