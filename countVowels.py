"""
Write a function that takes a string and returns the number of vowels (a, e, i, o, u) in it.
"""

def countVowels(s):
    vowels = { "a": 1, "e": 1, "i": 1,"o": 1, "u": 1}
    count = 0
    
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

"""
Brute force
def countVowels(s):
    count = 0
    for ch in s.lower():  # loop through each character in lowercase
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count
"""


print(countVowels("hello"))       # 2
print(countVowels("programming")) # 3
print(countVowels("PYTHON"))      # 1
print(countVowels("sky"))         # 0
