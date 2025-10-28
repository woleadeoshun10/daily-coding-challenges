"""
You are given an integer n.
Return True if n is a palindrome number (it reads the same forward and backward), otherwise return False.

Examples

Input: n = 121
Output: True
Explanation: 121 reads the same forward and backward.

Input: n = -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. So not the same.

Input: n = 10
Output: False
Explanation: 10 reversed is 01, not equal to 10.


"""

def isPalindrome(n):
    if n < 0:
        return False
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev == original
    
        
        
print(isPalindrome(+20393))       
print(isPalindrome(2635)) 
print(isPalindrome(121))     

"""
Brute Force
def isPalindrome(n):
    s = str(n)
    return s == s[::-1]
"""

