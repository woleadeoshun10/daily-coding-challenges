"""
🧩 Foundation Exercise 2: First Non-Repeating Character

👉 Problem:
Given a string, find the first character that does not repeat.

Example:
s = "aabbcddee" → Output: c

Hint:

Count frequency of each character using a dictionary.

Iterate again to find the first with frequency 1.
"""
def count_letters(word):
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
           
    for ch in word:
        if count[ch] < 2:
            return ch
            
    return None
 

word = "aabbccdedef"
print(count_letters(word))
